#app.py
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from base_datos import BaseDatos
from base_conocimiento import BaseConocimiento
from motor_inferencia import MotorDeInferencia

app = Flask(__name__)
app.secret_key = 'secret_key'  # Cambiar por una clave segura

# Inicializar instancias del sistema experto
db = BaseDatos()
base_conocimiento = BaseConocimiento()
motor_inferencia = MotorDeInferencia(base_conocimiento)

@app.context_processor
def inject_user():
    return dict(username=session.get('username'))

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el administrador
@app.route('/admin')
def admin_dashboard():
    if 'user_id' not in session or not db.es_administrador(session['user_id']):
        flash('Acceso denegado. Debe ser un administrador.', 'danger')
        return redirect(url_for('login'))

    total_usuarios = db.obtener_total_usuarios()
    total_tests = db.obtener_total_tests()
    pie_data = db.obtener_distribucion_clasificaciones()
    bar_data = db.obtener_tests_por_mes()
    ultimos_tests = db.obtener_ultimos_tests()
    ultimos_usuarios = db.obtener_ultimos_usuarios()

    return render_template(
        'admin_dashboard.html',
        total_usuarios=total_usuarios,
        total_tests=total_tests,
        pie_data=pie_data,
        bar_data=bar_data,
        ultimos_tests=ultimos_tests,
        ultimos_usuarios=ultimos_usuarios
    )



# Ruta principal: Página de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db.verificar_usuario(username, password)
        
        if user:
            session['user_id'] = user[0]  # ID del usuario
            session['rol_id'] = user[1]  # Rol del usuario
            session['username'] = username  # Nombre de usuario
            flash('Inicio de sesión exitoso.', 'success')

            # Redirigir según el rol
            if session['rol_id'] == 2:  # Administrador
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('welcome'))
        else:
            flash('Usuario o contraseña incorrectos.', 'danger')
    return render_template('login.html')


# Ruta para registrarse
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        sexo = request.form['sexo']
        edad = request.form['edad']
        correo = request.form['correo']
        carrera = request.form['carrera']
        ciclo = request.form['ciclo']
        if db.registrar_usuario(nombre, contrasena, sexo, edad, correo, carrera, ciclo):
            flash('Registro exitoso. Ahora puede iniciar sesión.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Error en el registro. Nombre de usuario ya existe.', 'danger')
    return render_template('register.html')

# Ruta de bienvenida
@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        flash('Por favor, inicie sesión primero.', 'warning')
        return redirect(url_for('login'))
    return render_template('welcome.html', username=session['username'])

# Ruta para realizar el test
@app.route('/test', methods=['GET', 'POST'])
def test():
    if 'user_id' not in session:
        flash('Por favor, inicie sesión primero.', 'warning')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        motor_inferencia.reset_test_data()
        
        # Procesar cada respuesta enviada
        for key, value in request.form.items():
            if key.startswith('respuestas['):  # Asegurarse de que la clave pertenece a las respuestas
                try:
                    idx = int(key.split('[')[1].split(']')[0])  # Extraer índice de la clave
                    respuesta = int(value)
                    pregunta = base_conocimiento.preguntas[idx]
                    motor_inferencia.evaluar_respuesta(respuesta, pregunta['factor'])
                except (ValueError, IndexError, KeyError) as e:
                    print(f"Error al procesar respuesta {key}: {e}")
        
        clasificacion = motor_inferencia.clasificar_depresion()
        factores = motor_inferencia.factores
        db.guardar_test(session['user_id'], factores, clasificacion)
        print(factores["Autoestima"])
        return redirect(url_for('results'))
    
    preguntas_con_indices = [
        {
            "idx": idx,
            "pregunta": pregunta["pregunta"],
            "opciones": list(enumerate(pregunta["opciones"]))
        }
        for idx, pregunta in enumerate(base_conocimiento.preguntas)
    ]
    return render_template('test.html', preguntas=preguntas_con_indices)


# Ruta para ver los resultados
@app.route('/results')
def results():
    if 'user_id' not in session:
        flash('Por favor, inicie sesión primero.', 'warning')
        return redirect(url_for('login'))
    clasificacion = motor_inferencia.clasificar_depresion()
    interpretacion = motor_inferencia.obtener_interpretacion_clasificacion(clasificacion)
    desglose_factores = motor_inferencia.generar_perfil_factores()
    recomendaciones = motor_inferencia.obtener_recomendaciones(clasificacion, motor_inferencia.factores)
    return render_template('results.html', 
                        puntuacion=motor_inferencia.puntuacion_total, 
                        clasificacion=clasificacion, 
                        interpretacion=interpretacion,
                        desglose_factores=desglose_factores,
                        recomendaciones=recomendaciones)

@app.route('/historial', methods=['GET'])
def historial():
    if 'user_id' not in session:  # Cambiado de 'usuario_id' a 'user_id'
        flash('Por favor, inicie sesión primero.', 'warning')
        return redirect(url_for('login'))

    user_id = session['user_id']
    historial_tests = db.obtener_historial_tests(usuario_id=user_id)

    historial_data = [
        {
            'fecha': str(test[7]),
            'clasificacion': test[6],
            'factores': {
                'Autoestima': test[0],
                'Pensamientos negativos': test[1],
                'Problemas interpersonales': test[2],
                'Ansiedad': test[3],
                'Función cognitiva': test[4],
                'Regulación emocional': test[5]
            }
        }
        for test in historial_tests
    ]

    return render_template('historial.html', historial=historial_data)

@app.route('/detalle_historial', methods=['POST'])
def detalle_historial():
    if 'user_id' not in session:
        return jsonify({"error": "Usuario no autenticado"}), 401

    user_id = session['user_id']
    data = request.get_json()
    if not data or 'fecha' not in data:
        return jsonify({"error": "Datos inválidos"}), 400

    fecha = data['fecha']
    historial_tests = db.obtener_historial_tests(usuario_id=user_id)

    for test in historial_tests:
        if str(test[7]) == fecha:
            # Calcula el resultado total como la suma de los puntajes de los factores
            resultado_total = sum([test[0], test[1], test[2], test[3], test[4], test[5]])

            return jsonify({
                'fecha': str(test[7]),
                'clasificacion': test[6],
                'resultado_total': resultado_total,  # Agregado
                'factores': {
                    'Autoestima': test[0],
                    'Pensamientos negativos': test[1],
                    'Problemas interpersonales': test[2],
                    'Ansiedad': test[3],
                    'Función cognitiva': test[4],
                    'Regulación emocional': test[5]
                }
            })

    return jsonify({"error": "Registro no encontrado"}), 404

@app.route('/filter_pie_chart')
def filter_pie_chart():
    month = request.args.get('month', type=int)
    year = request.args.get('year', type=int)

    filtered_data = db.obtener_distribucion_clasificaciones_filtrada(month, year)
    return jsonify(filtered_data)

@app.route('/usuarios')
def admin_usuarios():
    if 'user_id' not in session or not db.es_administrador(session['user_id']):
        flash('Acceso denegado. Debe ser un administrador.', 'danger')
        return redirect(url_for('login'))

    usuarios = db.obtener_usuarios()  # Obtiene todos los usuarios registrados
    return render_template('admin_usuarios.html', usuarios=usuarios)

@app.route('/usuario_detalle/<int:id>', methods=['GET'])
def usuario_detalle(id):
    if 'user_id' not in session or not db.es_administrador(session['user_id']):
        return jsonify({"error": "Acceso denegado"}), 403

    usuario = db.obtener_usuario_por_id(id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    return jsonify(usuario)

@app.route('/admin/tests', methods=['GET'])
def admin_tests():
    if 'user_id' not in session or not db.es_administrador(session['user_id']):
        flash('Acceso denegado: solo administradores pueden ver esta página.', 'danger')
        return redirect(url_for('login'))

    historial_tests = db.obtener_historial_completo()

    historial_data = [
        {
            'nombre_usuario': test['nombre_usuario'],
            'fecha': str(test['fecha']),
            'clasificacion': test['clasificacion'],
            'usuario_id': test['usuario_id']
        }
        for test in historial_tests
    ]

    return render_template('admin_historial_tests.html', historial=historial_data)

@app.route('/admin/tests/detalle', methods=['POST'])
def admin_test_detalle():
    if 'user_id' not in session or not db.es_administrador(session['user_id']):
        return jsonify({"error": "Acceso denegado: solo administradores pueden acceder."}), 403

    data = request.get_json()
    if not data or 'fecha' not in data or 'usuario_id' not in data:
        return jsonify({"error": "Datos inválidos."}), 400

    fecha = data['fecha']
    usuario_id = data['usuario_id']

    historial_tests = db.obtener_historial_tests(usuario_id=usuario_id)

    for test in historial_tests:
        if str(test[7]) == fecha:
            resultado_total = sum([test[0], test[1], test[2], test[3], test[4], test[5]])

            return jsonify({
                'nombre_usuario': db.obtener_usuario_por_id(usuario_id)['nombre'],
                'fecha': str(test[7]),
                'clasificacion': test[6],
                'resultado_total': resultado_total,
                'factores': {
                    'Autoestima': test[0],
                    'Pensamientos negativos': test[1],
                    'Problemas interpersonales': test[2],
                    'Ansiedad': test[3],
                    'Función cognitiva': test[4],
                    'Regulación emocional': test[5]
                }
            })

    return jsonify({"error": "Registro no encontrado."}), 404


# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.clear()
    flash('Sesión cerrada exitosamente.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
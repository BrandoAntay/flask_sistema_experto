#base_datos.py

import mysql.connector
import bcrypt
from datetime import datetime

class BaseDatos:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="Brando",
            password="9012450405",
            database="sistema_experto"
        )
        self.cursor = self.conexion.cursor()
        self.crear_tablas()

    def crear_tablas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) UNIQUE NOT NULL,
                contrasena VARCHAR(255) NOT NULL,
                sexo ENUM('hombre', 'mujer') NOT NULL,
                edad INT NOT NULL,
                correo_electronico VARCHAR(255) NOT NULL,
                carrera ENUM('Ing. de Sistemas', 'Administracion', 'Contabilidad', 'Agronomia', 'Turismo y Hoteleria') NOT NULL,
                ciclo ENUM('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'VIIII', 'X') NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS historial_tests (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario_id INT,
                puntaje_total INT,
                clasificacion VARCHAR(255),
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
            )
        ''')
        self.conexion.commit()

    def registrar_usuario(self, nombre_usuario, contrasena, sexo, edad, correo_electronico, carrera, ciclo):
        try:
            hashed_password = bcrypt.hashpw(
                contrasena.encode('utf-8'), bcrypt.gensalt())
            self.cursor.execute(
                "INSERT INTO usuarios (nombre, contrasena, sexo, edad, correo_electronico, carrera, ciclo) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (nombre_usuario, hashed_password.decode('utf-8'), sexo, edad, correo_electronico, carrera, ciclo)
            )
            self.conexion.commit()
            return True
        except mysql.connector.IntegrityError:
            return False

    def verificar_usuario(self, nombre_usuario, contrasena):
        # Seleccionar id y rol_id del usuario
        query = "SELECT id, contrasena, rol_id FROM usuarios WHERE nombre = %s"
        self.cursor.execute(query, (nombre_usuario,))
        user = self.cursor.fetchone()

        # Verificar si la contraseña coincide
        if user and bcrypt.checkpw(contrasena.encode('utf-8'), user[1].encode('utf-8')):
            return user[0], user[2]  # Devuelve id y rol_id
        return None



    def guardar_test(self, usuario_id, factores, clasificacion):
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(
            """
            INSERT INTO historial_tests (usuario_id, autoestima, pensamientos_negativos, problemas_interpersonales,
                                        ansiedad, funcion_cognitiva, regulacion_emocional, clasificacion, fecha)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                usuario_id,
                factores.get("Autoestima", 0),
                factores.get("Pensamientos negativos", 0),
                factores.get("Problemas interpersonales", 0),
                factores.get("Ansiedad", 0),
                factores.get("Función cognitiva", 0),
                factores.get("Regulación emocional", 0),
                clasificacion,
                fecha_actual
            )
        )
        self.conexion.commit()


    def obtener_historial_tests(self, usuario_id=None):
        if usuario_id:
            self.cursor.execute(
                """
                SELECT autoestima, pensamientos_negativos, problemas_interpersonales,
                    ansiedad, funcion_cognitiva, regulacion_emocional, clasificacion, fecha
                FROM historial_tests
                WHERE usuario_id = %s
                ORDER BY fecha DESC
                """,
                (usuario_id,)
            )
        else:
            self.cursor.execute(
                """
                SELECT usuarios.nombre, historial_tests.autoestima, historial_tests.pensamientos_negativos,
                    historial_tests.problemas_interpersonales, historial_tests.ansiedad,
                    historial_tests.funcion_cognitiva, historial_tests.regulacion_emocional,
                    historial_tests.clasificacion, historial_tests.fecha
                FROM historial_tests
                INNER JOIN usuarios ON historial_tests.usuario_id = usuarios.id
                """
            )
        return self.cursor.fetchall()

    # Verificar si el usuario tiene rol de administrador
    def es_administrador(self, user_id):
        query = "SELECT rol_id FROM usuarios WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        result = self.cursor.fetchone()
        return result and result[0] == 2  # Verifica si el rol es 'Administrador'

    # Obtener el total de usuarios registrados
    def obtener_total_usuarios(self):
        query = "SELECT COUNT(*) FROM usuarios"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    # Obtener el total de tests realizados
    def obtener_total_tests(self):
        query = "SELECT COUNT(*) FROM historial_tests"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def obtener_distribucion_clasificaciones(self):
        # Lista base de clasificaciones
        clasificaciones_base = ["Mínima depresión", "Depresión leve", "Depresión moderada", "Depresión grave"]

        # Consulta para obtener las clasificaciones existentes y sus conteos
        query = """
            SELECT clasificacion, COUNT(*) AS total
            FROM historial_tests
            GROUP BY clasificacion
        """
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()

        # Crear un diccionario con las clasificaciones base y valores iniciales en 0
        clasificaciones_dict = {clasificacion: 0 for clasificacion in clasificaciones_base}

        # Actualizar el diccionario con los valores obtenidos de la base de datos
        for clasificacion, total in resultados:
            clasificaciones_dict[clasificacion] = total

        # Preparar datos para el gráfico
        labels = list(clasificaciones_dict.keys())
        values = list(clasificaciones_dict.values())

        return {"labels": labels, "values": values}

    def obtener_distribucion_clasificaciones_filtrada(self, month, year):
        clasificaciones_base = ["Mínima depresión", "Depresión leve", "Depresión moderada", "Depresión grave"]

        query = """
            SELECT clasificacion, COUNT(*) AS total
            FROM historial_tests
            WHERE MONTH(fecha) = %s AND YEAR(fecha) = %s
            GROUP BY clasificacion
        """
        self.cursor.execute(query, (month, year))
        resultados = self.cursor.fetchall()

        clasificaciones_dict = {clasificacion: 0 for clasificacion in clasificaciones_base}
        for clasificacion, total in resultados:
            clasificaciones_dict[clasificacion] = total

        labels = list(clasificaciones_dict.keys())
        values = list(clasificaciones_dict.values())

        return {"labels": labels, "values": values}


    def obtener_tests_por_mes(self):
        query = """
            SELECT MONTH(fecha) AS mes, COUNT(*) AS total
            FROM historial_tests
            WHERE YEAR(fecha) = YEAR(CURDATE())
            GROUP BY MONTH(fecha)
            ORDER BY mes
        """
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()
        labels = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        values = [0] * 12  # Inicializar con ceros para todos los meses
        for row in resultados:
            values[row[0] - 1] = row[1]  # Mapear el total al mes correspondiente
        return {"labels": labels, "values": values}

    def obtener_ultimos_tests(self):
        query = """
            SELECT usuarios.nombre, historial_tests.clasificacion, historial_tests.fecha
            FROM historial_tests
            INNER JOIN usuarios ON historial_tests.usuario_id = usuarios.id
            ORDER BY historial_tests.fecha DESC
            LIMIT 10
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def obtener_ultimos_usuarios(self):
        query = """
            SELECT nombre, correo_electronico, fecha_registro
            FROM usuarios
            ORDER BY fecha_registro DESC
            LIMIT 10
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def obtener_usuarios(self):
        query = """
            SELECT usuarios.id, usuarios.nombre, usuarios.sexo, usuarios.edad, 
                usuarios.correo_electronico, usuarios.carrera, usuarios.ciclo, 
                rol.nombre AS rol, usuarios.fecha_registro
            FROM usuarios
            INNER JOIN rol ON usuarios.rol_id = rol.id
        """
        self.cursor.execute(query)
        usuarios = self.cursor.fetchall()
        return [
            {
                "id": usuario[0],
                "nombre": usuario[1],
                "sexo": usuario[2],
                "edad": usuario[3],
                "correo": usuario[4],
                "carrera": usuario[5],
                "ciclo": usuario[6],
                "rol": usuario[7],
                "fecha_registro": usuario[8]
            }
            for usuario in usuarios
        ]

    def obtener_usuario_por_id(self, usuario_id):
        query = """
            SELECT usuarios.id, usuarios.nombre, usuarios.correo_electronico, usuarios.carrera, usuarios.ciclo,
                usuarios.sexo, usuarios.edad, rol.nombre AS rol, usuarios.fecha_registro
            FROM usuarios
            INNER JOIN rol ON usuarios.rol_id = rol.id
            WHERE usuarios.id = %s
        """
        self.cursor.execute(query, (usuario_id,))
        resultado = self.cursor.fetchone()

        if resultado:
            return {
                "id": resultado[0],  # Asegúrate de incluir el ID
                "nombre": resultado[1],
                "correo": resultado[2],
                "carrera": resultado[3],
                "ciclo": resultado[4],
                "sexo": resultado[5],
                "edad": resultado[6],
                "rol": resultado[7],
                "fecha_registro": resultado[8],
            }
        return None

    def obtener_historial_completo(self):
        query = """
            SELECT u.nombre AS nombre_usuario, h.autoestima, h.pensamientos_negativos,
                h.problemas_interpersonales, h.ansiedad, h.funcion_cognitiva,
                h.regulacion_emocional, h.clasificacion, h.fecha, h.usuario_id
            FROM historial_tests h
            INNER JOIN usuarios u ON h.usuario_id = u.id
            ORDER BY h.fecha DESC
        """
        self.cursor.execute(query)
        historial = self.cursor.fetchall()
        return [
            {
                "nombre_usuario": row[0],
                "autoestima": row[1],
                "pensamientos_negativos": row[2],
                "problemas_interpersonales": row[3],
                "ansiedad": row[4],
                "funcion_cognitiva": row[5],
                "regulacion_emocional": row[6],
                "clasificacion": row[7],
                "fecha": row[8],
                "usuario_id": row[9],
            }
            for row in historial
        ]




    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
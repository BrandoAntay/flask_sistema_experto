class MotorDeInferencia:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento
        self.puntuacion_total = 0
        self.factores = {
            "Autoestima": 0,
            "Pensamientos negativos": 0,
            "Problemas interpersonales": 0,
            "Ansiedad": 0,
            "Función cognitiva": 0,
            "Regulación emocional": 0,
        }

    def reset_test_data(self):
        """Reinicia los datos del test."""
        self.puntuacion_total = 0
        self.factores = {factor: 0 for factor in self.factores}

    def evaluar_respuesta(self, respuesta, factor):
        """Acumula la respuesta en la puntuación total y en el factor correspondiente."""
        print(f"Procesando respuesta: {respuesta} para factor: {factor}")  # Agregado para depuración
        self.puntuacion_total += respuesta
        self.factores[factor] += respuesta

    def clasificar_depresion(self):
        """Clasifica el nivel de depresión basado en la puntuación total."""
        for clasificacion, (min_puntaje, max_puntaje) in self.base_conocimiento.clasificaciones.items():
            if min_puntaje <= self.puntuacion_total <= max_puntaje:
                return clasificacion
        return "Clasificación no disponible"

    def obtener_interpretacion_clasificacion(self, clasificacion):
        """Obtiene la interpretación correspondiente a una clasificación de depresión."""
        return self.base_conocimiento.interpretaciones_clasificacion.get(clasificacion, "No hay interpretación disponible para esta clasificación.")

    def generar_perfil_factores(self):
        """Genera un perfil detallado por factor en porcentaje y devuelve interpretaciones."""
        perfil_factores = {}
        for factor, puntaje in self.factores.items():
            total_puntaje_factor = len([p for p in self.base_conocimiento.preguntas if p['factor'] == factor]) * 3
            porcentaje = (puntaje / total_puntaje_factor) * 100 if total_puntaje_factor > 0 else 0
            if porcentaje < 25:
                interpretacion = "Sin indicios significativos en este factor."
            elif porcentaje < 50:
                interpretacion = "Indicadores leves en este factor."
            elif porcentaje < 75:
                interpretacion = "Indicadores moderados en este factor."
            else:
                interpretacion = "Indicadores altos en este factor, es recomendable prestar atención."
            perfil_factores[factor] = f"{puntaje} puntos ({porcentaje:.2f}%) - {interpretacion}"
        return perfil_factores

    def obtener_recomendaciones(self, clasificacion, factores):
        """Obtiene recomendaciones basadas en la clasificación y los factores relevantes."""
        recomendaciones = self.base_conocimiento.recomendaciones_clasificacion.get(clasificacion, [])
        for factor, puntaje in factores.items():
            if puntaje > 5 and factor in self.base_conocimiento.recomendaciones_por_factor:
                recomendaciones.append(self.base_conocimiento.recomendaciones_por_factor[factor])
        return "\n".join(recomendaciones) if recomendaciones else "No se requieren recomendaciones adicionales en este momento."

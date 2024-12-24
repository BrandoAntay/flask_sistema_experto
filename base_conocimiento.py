# base_conocimiento.py

class BaseConocimiento:
    def __init__(self):
        # Cada pregunta está relacionada con un factor y tiene opciones sin el valor numérico al inicio
        self.preguntas = [
            {"pregunta": "Tristeza", "opciones": [
                "No me siento triste.",
                "Me siento triste gran parte del tiempo.",
                "Estoy triste todo el tiempo.",
                "Estoy triste o soy tan infeliz que no puedo soportarlo."
            ], "factor": "Autoestima"},
            
            {"pregunta": "Pesimismo", "opciones": [
                "No estoy desalentado respecto de mi futuro.",
                "Me siento más desalentado respecto de mi futuro que lo que solía estarlo.",
                "No espero que las cosas funcionen para mí.",
                "Siento que no hay esperanza para mi futuro y que sólo puede empeorar."
            ], "factor": "Pensamientos negativos"},
            
            {"pregunta": "Sentimientos de Fracaso", "opciones": [
                "No me siento como un fracasado.",
                "He fracasado más de lo que hubiera debido.",
                "Cuando miro hacia atrás veo muchos fracasos.",
                "Siento que como persona soy un fracaso total."
            ], "factor": "Autoestima"},
            
            {"pregunta": "Pérdida del Placer", "opciones": [
                "Obtengo tanto placer como siempre por las cosas de las que disfruto.",
                "No disfruto tanto de las cosas como solía hacerlo.",
                "Obtengo muy poco placer de las cosas de las que solía disfrutar.",
                "No puedo obtener ningún placer de las cosas de las que solía disfrutar."
            ], "factor": "Problemas interpersonales"},
            
            {"pregunta": "Sentimientos de Culpa", "opciones": [
                "No me siento particularmente culpable.",
                "Me siento culpable respecto de varias cosas que he hecho o que debería haber hecho.",
                "Me siento bastante culpable la mayor parte del tiempo.",
                "Me siento culpable todo el tiempo."
            ], "factor": "Autoestima"},
            
            {"pregunta": "Sentimientos de Castigo", "opciones": [
                "No siento que estoy siendo castigado.",
                "Siento que tal vez pueda ser castigado.",
                "Espero ser castigado.",
                "Siento que estoy siendo castigado."
            ], "factor": "Pensamientos negativos"},
            
            {"pregunta": "Aversión a uno mismo", "opciones": [
                "Siento acerca de mí lo mismo que siempre.",
                "He perdido la confianza en mí mismo.",
                "Estoy decepcionado conmigo mismo.",
                "No me gusto a mí mismo."
            ], "factor": "Autoestima"},
            
            {"pregunta": "Autocrítica", "opciones": [
                "No me critico ni me culpo más de lo habitual.",
                "Estoy más crítico conmigo mismo de lo que solía estarlo.",
                "Me critico a mí mismo por todos mis errores.",
                "Me culpo a mí mismo por todo lo malo que sucede."
            ], "factor": "Autoestima"},
            
            {"pregunta": "Pensamientos de Suicidio", "opciones": [
                "No tengo ningún pensamiento de matarme.",
                "He tenido pensamientos de matarme, pero no lo haría.",
                "Querría matarme.",
                "Me mataría si tuviera la oportunidad de hacerlo."
            ], "factor": "Pensamientos negativos"},
            
            {"pregunta": "Llanto", "opciones": [
                "No lloro más de lo que solía hacerlo.",
                "Lloro más de lo que solía hacerlo.",
                "Lloro por cualquier pequeñez.",
                "Siento ganas de llorar pero no puedo."
            ], "factor": "Regulación emocional"},
            
            {"pregunta": "Agitación", "opciones": [
                "No estoy más inquieto o tenso que lo habitual.",
                "Me siento más inquieto o tenso que lo habitual.",
                "Estoy tan inquieto o agitado que me es difícil quedarme quieto.",
                "Estoy tan inquieto o agitado que tengo que estar siempre en movimiento."
            ], "factor": "Ansiedad"},
            
            {"pregunta": "Pérdida del Interés", "opciones": [
                "No he perdido el interés en otras actividades o personas.",
                "Estoy menos interesado que antes en otras personas o cosas.",
                "He perdido casi todo el interés en otras personas o cosas.",
                "Me es difícil interesarme por algo."
            ], "factor": "Problemas interpersonales"},
            
            {"pregunta": "Indecisión", "opciones": [
                "Tomo mis decisiones tan bien como siempre.",
                "Me resulta más difícil que de costumbre tomar decisiones.",
                "Encuentro mucha más dificultad que antes para tomar decisiones.",
                "Tengo problemas para tomar cualquier decisión."
            ], "factor": "Función cognitiva"},
            
            {"pregunta": "Inutilidad", "opciones": [
                "No siento que yo no sea valioso.",
                "No me considero a mí mismo tan valioso y útil como solía considerarme.",
                "Me siento menos valioso cuando me comparo con otros.",
                "Siento que no valgo nada."
            ], "factor": "Autoestima"},
            
            {"pregunta": "Pérdida de la Energía", "opciones": [
                "Tengo tanta energía como siempre.",
                "Tengo menos energía que la que solía tener.",
                "No tengo suficiente energía para hacer demasiado.",
                "No tengo energía suficiente para hacer nada."
            ], "factor": "Función cognitiva"},
            
            {"pregunta": "Cambios en el patrón de Sueño", "opciones": [
                "No he experimentado ningún cambio en mis hábitos de sueño.",
                "Duermo un poco menos de lo habitual.",
                "Duermo mucho menos que lo habitual.",
                "Me despierto 1-2 horas más temprano y no puedo volver a dormirme."
            ], "factor": "Ansiedad"},
            
            {"pregunta": "Irritabilidad", "opciones": [
                "No estoy más irritable que lo habitual.",
                "Estoy más irritable que lo habitual.",
                "Estoy mucho más irritable que lo habitual.",
                "Estoy irritable todo el tiempo."
            ], "factor": "Regulación emocional"},
            
            {"pregunta": "Cambios en el Apetito", "opciones": [
                "No he experimentado ningún cambio en mi apetito.",
                "Mi apetito es un poco mayor que lo habitual.",
                "Mi apetito es mucho mayor que lo habitual.",
                "Quiero comer todo el tiempo."
            ], "factor": "Ansiedad"},
            
            {"pregunta": "Dificultad de Concentración", "opciones": [
                "Puedo concentrarme tan bien como siempre.",
                "No puedo concentrarme tan bien como habitualmente.",
                "Me es difícil mantener la mente en algo por mucho tiempo.",
                "Encuentro que no puedo concentrarme en nada."
            ], "factor": "Función cognitiva"},
            
            {"pregunta": "Cansancio o Fatiga", "opciones": [
                "No estoy más cansado o fatigado que lo habitual.",
                "Me fatigo o me canso más fácilmente que lo habitual.",
                "Estoy demasiado fatigado o cansado para hacer muchas de las cosas que solía hacer.",
                "Estoy demasiado fatigado o cansado para hacer la mayoría de las cosas que solía hacer."
            ], "factor": "Función cognitiva"},
            
            {"pregunta": "Pérdida de Interés en el Sexo", "opciones": [
                "No he notado ningún cambio reciente en mi interés por el sexo.",
                "Estoy menos interesado en el sexo de lo que solía estarlo.",
                "Ahora estoy mucho menos interesado en el sexo.",
                "He perdido completamente el interés en el sexo."
            ], "factor": "Problemas interpersonales"},
        ]
        
        # Clasificación de la depresión según puntuaciones
        self.clasificaciones = {
            "Mínima depresión": (0, 13),
            "Depresión leve": (14, 19),
            "Depresión moderada": (20, 28),
            "Depresión grave": (29, 63)
        }
        
        # Interpretación para cada clasificación
        self.interpretaciones_clasificacion = {
            "Mínima depresión": "No se observan síntomas significativos de depresión.",
            "Depresión leve": "Algunos síntomas de depresión afectan la vida diaria, pero son manejables.",
            "Depresión moderada": "Síntomas claros que afectan el bienestar y pueden requerir ayuda profesional.",
            "Depresión grave": "Síntomas intensos que afectan gravemente la vida. Se recomienda buscar ayuda profesional."
        }
        
        # Recomendaciones para cada factor en base al puntaje
        self.recomendaciones_por_factor = {
            "Autoestima": "Realizar ejercicios de autoaceptación y gratitud para mejorar la autoestima.",
            "Pensamientos negativos": "Iniciar terapia para manejo de pensamientos negativos y prevención de conductas autolesivas.",
            "Ansiedad": "Técnicas de relajación y mindfulness para controlar la ansiedad.",
            "Función cognitiva": "Realizar ejercicios de estimulación cognitiva y técnicas de mejora de la concentración.",
            "Regulación emocional": "Terapia enfocada en la regulación emocional y manejo del estrés.",
            "Problemas interpersonales": "Fortalecer habilidades de comunicación y establecer relaciones de apoyo."
        }
        
        # Recomendaciones específicas para la clasificación general
        self.recomendaciones_clasificacion = {
            "Depresión grave": [
                "Se recomienda consultar a un especialista de inmediato.",
                "Considerar terapia cognitivo-conductual intensiva.",
                "Evaluar apoyo farmacológico."
            ],
            "Depresión moderada": [
                "Considerar consultar a un profesional de salud mental para evaluación.",
                "Incorporar actividades de autocuidado en la vida diaria."
            ],
            "Depresión leve": [
                "Mantener una red de apoyo y practicar técnicas de manejo del estrés.",
                "Considerar un programa de terapia breve o sesiones de coaching."
            ],
            "Mínima depresión": [
                "Practicar hábitos de vida saludable para mantener el bienestar emocional.",
                "Continuar con actividades que promuevan el bienestar psicológico."
            ]
        }
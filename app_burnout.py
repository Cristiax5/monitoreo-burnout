import streamlit as st

# Configuración principal de la página (Diseño Clínico)
st.set_page_config(
    page_title="Monitoreo de Burnout Clínico", 
    page_icon="🩺", 
    layout="centered"
)

# Inicializar las variables de la sesión
if "registrado" not in st.session_state:
    st.session_state.registrado = False
if "nombre_usuario" not in st.session_state:
    st.session_state.nombre_usuario = ""
if "rol_usuario" not in st.session_state:
    st.session_state.rol_usuario = ""

# ==========================================
# INTERFAZ DE REGISTRO / INICIO
# ==========================================
if not st.session_state.registrado:
    st.markdown("<h1 style='text-align: center; color: #004b49;'>🩺 Sistema de Evaluación de Burnout</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #555555;'>Módulo de Monitoreo Dinámico y Prevención</h4>", unsafe_allow_html=True)
    
    st.info("🔒 Por favor, ingresa tus datos en el formulario médico de abajo para desbloquear tu evaluación personalizada.")
    
    # Caja visual para el formulario
    with st.container():
        nombre = st.text_input("👤 Nombre Completo o Iniciales:", placeholder="Ej. Dr. J. Pérez o Alumno M. Gómez")
        rol = st.selectbox(
            "📋 Selecciona tu Rol Actual:", 
            [
                "Estudiante de Ciencias de la Salud / Pregrado", 
                "Médico Interno / Residente / Carga Hospitalaria", 
                "Profesional de la Salud Activo"
            ]
        )
        st.markdown("---")
        
        if st.button("🔓 Iniciar Evaluación Clínica", type="primary", use_container_width=True):
            if nombre.strip() == "":
                st.error("⚠️ El campo de nombre es obligatorio para el registro clínico.")
            else:
                st.session_state.nombre_usuario = nombre
                st.session_state.rol_usuario = rol
                st.session_state.registrado = True
                st.rerun()

# ==========================================
# INTERFAZ INTERACTIVA (CUESTIONARIO DINÁMICO)
# ==========================================
else:
    # Barra lateral con información del usuario
    with st.sidebar:
        st.markdown("<h3 style='color: #004b49;'>👤 Expediente Activo</h3>", unsafe_allow_html=True)
        st.write(f"**Evaluado:** {st.session_state.nombre_usuario}")
        st.write(f"**Sector:** {st.session_state.rol_usuario}")
        st.markdown("---")
        if st.button("❌ Cerrar Sesión y Salir"):
            st.session_state.registrado = False
            st.session_state.nombre_usuario = ""
            st.rerun()

    # Título principal de la evaluación
    st.markdown(f"<h2 style='color: #004b49;'>📊 Evaluación Interactiva: {st.session_state.nombre_usuario}</h2>", unsafe_allow_html=True)
    st.caption(f"Cuestionario adaptado para el perfil: **{st.session_state.rol_usuario}**")
    st.markdown("---")
    
    st.subheader("📋 Escala de Frecuencia de Síntomas")
    st.write("Selecciona el valor que mejor describa tus últimas semanas: *(0 = Nunca | 3 = A veces | 6 = Todos los días)*")

    # 🧠 BANCO DE PREGUNTAS DINÁMICAS (Cambian según el Rol)
    preguntas = []
    
    if "Estudiante" in st.session_state.rol_usuario:
        preguntas = [
            "1. ¿Te sientes emocionalmente agotado por la carga de materias, tareas y exámenes?",
            "2. ¿Te cuesta más trabajo levantarte por la mañana para ir a clases o a tus prácticas?",
            "3. ¿Sientes que has perdido el entusiasmo por tu carrera o tus estudios?",
            "4. ¿Te frustras o te pones de mal humor con facilidad si tus notas no son perfectas?",
            "5. ¿Sientes que estás demasiado estresado para absorber y memorizar nuevos conocimientos?",
            "6. ¿Consideras que la presión por mantener buenas calificaciones afecta tu apetito o sueño?",
            "7. ¿Te has alejado de tus amigos o actividades recreativas por falta de energía académica?",
            "8. ¿Dudas de tu capacidad para terminar con éxito tus estudios de la salud?",
            "9. ¿Sientes ansiedad intensa antes de una evaluación académica o simulación clínica?",
            "10. ¿Al final de la semana te sientes completamente exhausto y sin ganas de hacer nada?"
        ]
    else:
        # Preguntas para Médicos Internos, Residentes o Profesionales
        preguntas = [
            "1. ¿Te sientes emocionalmente agotado por el exceso de horas de jornada laboral o guardias?",
            "2. ¿Sientes cansancio extremo incluso antes de iniciar tu turno en el hospital o clínica?",
            "3. ¿Sientes que te has vuelto más frío, distante o cínico con los pacientes o compañeros?",
            "4. ¿Te frustras con rapidez ante complicaciones médicas o imprevistos en tu jornada?",
            "5. ¿Consideras que la falta de descanso está afectando tu concentración o rendimiento clínico?",
            "6. ¿Sientes que el tiempo que dedicas a tu profesión te impide tener una vida personal saludable?",
            "7. ¿Te preocupa cometer algún error debido al cansancio acumulado?",
            "8. ¿Sientes que tus superiores o la institución no valoran adecuadamente tu esfuerzo diario?",
            "9. ¿Experimentas síntomas físicos de estrés (dolor de cabeza, tensión) durante tu labor?",
            "10. ¿Has llegado a pensar que elegiste la profesión equivocada debido al nivel de desgaste?"
        ]

    # Crear los 10 Sliders interactivos dinámicamente
    respuestas = []
    for q in preguntas:
        v = st.slider(q, 0, 6, 0, key=q)
        respuestas.append(v)

    st.markdown("---")

    # 🚀 CÁLCULO Y DIAGNÓSTICO
    if st.button("🎯 Procesar Diagnóstico de Estrés", type="primary", use_container_width=True):
        puntaje_total = sum(respuestas)
        max_puntaje = 60 # 10 preguntas x 6 puntos max
        
        st.markdown("<h3 style='color: #004b49;'>🎯 Diagnóstico de la Evaluación</h3>", unsafe_allow_html=True)
        st.metric(label="Índice de Desgaste Emocional", value=f"{puntaje_total} / {max_puntaje} pts")
        
        # Lógica de semáforo clínico
        if puntaje_total <= 20:
            st.balloons() # 🎉 Animación de globos por buen estado
            st.success(f"🟢 **Nivel Bajo / Normal:** ¡Excelente, {st.session_state.nombre_usuario}! Te encuentras en un rango estable de salud mental y laboral. Sigue manteniendo tus espacios de esparcimiento.")
        elif 21 <= puntaje_total <= 40:
            st.warning(f"🟡 **Nivel Moderado (Fase de Alerta):** Presentas signos de estrés acumulado, {st.session_state.nombre_usuario}. Es recomendable que busques organizar mejor tus tiempos y comiences a implementar técnicas de relajación.")
        else:
            st.error(f"🔴 **Nivel Severo (Alerta Crítica de Burnout):** {st.session_state.nombre_usuario}, tus niveles de agotamiento son muy elevados. Es de suma importancia que delegues responsabilidades, extremes precauciones y consideres consultar con un especialista.")
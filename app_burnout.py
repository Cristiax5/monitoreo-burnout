import streamlit as st
import datetime

# Configuración de la página con estilo moderno y limpio
st.set_page_config(
    page_title="Mente Sana - ¡Cuida tu energía!", 
    page_icon="🧠", 
    layout="centered"
)

# ==========================================
# SISTEMA DE RACHA Y MASCOTA (INICIALIZACIÓN)
# ==========================================
if "registrado" not in st.session_state:
    st.session_state.registrado = False
if "nombre_usuario" not in st.session_state:
    st.session_state.nombre_usuario = ""
if "carrera_usuario" not in st.session_state:
    st.session_state.carrera_usuario = ""

# Datos simulados de racha diaria
if "racha_dias" not in st.session_state:
    st.session_state.racha_dias = 1
if "ultimo_test" not in st.session_state:
    st.session_state.ultimo_test = None

# Función para simular el paso de los días y actualizar la racha
def actualizar_racha():
    hoy = datetime.date.today()
    if st.session_state.ultimo_test is not None:
        ayer = hoy - datetime.timedelta(days=1)
        if st.session_state.ultimo_test == ayer:
            st.session_state.racha_dias += 1
        elif st.session_state.ultimo_test < ayer:
            st.session_state.racha_dias = 1  # Se rompió la racha
    st.session_state.ultimo_test = hoy

# Función para mostrar a la mascota según la racha
def obtener_mascota(racha):
    if racha == 1:
        return "🥚", "¡Tu mascota acaba de nacer! Es un huevito. Haz tu test mañana para que rompa el cascarón."
    elif racha == 2:
        return "🐥", "¡Ya nació! Tu pollito de la racha está feliz de verte hoy."
    elif racha == 3:
        return "🦉", "¡Ha evolucionado a un Búho Sabio! Te acompaña en tus noches de estudio."
    elif racha <= 5:
        return "🦊", f"¡Un Zorro Aventurero! Llevas {racha} días cuidando tu mente, ¡está orgulloso de ti!"
    else:
        return "🐉", f"🔥 ¡NIVEL MÁXIMO! Un Dragón Zen. ¡Llevas una racha brutal de {racha} días seguidos!"

# ==========================================
# PANTALLA DE INICIO (DISEÑO SÚPER AGRADABLE)
# ==========================================
if not st.session_state.registrado:
    st.markdown("""
        <div style='background: linear-gradient(135deg, #1565C0 0%, #1E88E5 100%); padding: 35px; border-radius: 20px; box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.1); text-align: center; margin-bottom: 25px;'>
            <h1 style='color: white; margin: 0; font-family: "Helvetica Neue", sans-serif; font-size: 38px; font-weight: 700;'>🧠 Mente Sana</h1>
            <p style='color: #E3F2FD; font-size: 18px; margin-top: 10px; font-weight: 300; letter-spacing: 0.5px;'>Tu espacio seguro para medir, entender y cuidar tus niveles de estrés académico y laboral.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style='background-color: #F5F5F5; padding: 18px; border-radius: 12px; border-left: 5px solid #1565C0; margin-bottom: 20px;'>
            <span style='color: #424242; font-size: 15px; font-weight: 500;'>👋 <b>¡Hola! Queremos darte una experiencia personalizada.</b> Cuéntanos un poco sobre ti para adaptar las preguntas a tu día a día de forma inteligente.</span>
        </div>
    """, unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown("<p style='color: #1565C0; font-weight: bold; margin-bottom: 5px;'>✨ Datos del Evaluado</p>", unsafe_allow_html=True)
        nombre = st.text_input("¿Cómo te gusta que te llamen? (Nombre o Apodo):", placeholder="Ej. Ani / Fer / Mau")
        
        st.markdown("<p style='color: #1565C0; font-weight: bold; margin-top: 15px; margin-bottom: 5px;'>🎓 Tu Entorno Diario</p>", unsafe_allow_html=True)
        carrera = st.selectbox("¿Qué carrera estás estudiando actualmente?", ["Medicina", "Enfermería", "Nutrición", "Odontología", "Psicología", "Otro"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("¡Comenzar mi Test ahora! 🚀", type="primary", use_container_width=True):
        if nombre.strip() == "":
            st.warning("⚠️ ¡Hey! No olvides escribir tu nombre para poder saludarte de verdad al iniciar.")
        else:
            st.session_state.nombre_usuario = nombre
            st.session_state.carrera_usuario = carrera
            st.session_state.registrado = True
            st.rerun()

# ==========================================
# CUESTIONARIO Y PANEL DE MASCOTA
# ==========================================
else:
    # Encabezado dinámico y colorido en el test
    st.markdown(f"""
        <div style='background-color: #E8F5E9; padding: 18px; border-radius: 15px; margin-bottom: 25px; border-left: 5px solid #2E7D32;'>
            <h2 style='color: #2E7D32; margin: 0; font-size: 24px;'>📊 Test Personalizado: {st.session_state.carrera_usuario}</h2>
            <p style='color: #388E3C; margin: 5px 0 0 0; font-size: 15px;'>¡Vamos con todo, <b>{st.session_state.nombre_usuario}</b>! Responde basándote en tus últimas semanas.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 🐾 RECUADRO DE LA MASCOTA DE RACHA
    avatar, estado_mascota = obtener_mascota(st.session_state.racha_dias)
    
    with st.container(border=True):
        col1, col2 = st.columns([1, 4])
        with col1:
            st.markdown(f"<h1 style='text-align: center; font-size: 60px; margin: 0;'>{avatar}</h1>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"### 🔥 Racha Activa: **{st.session_state.racha_dias} { 'día' if st.session_state.racha_dias == 1 else 'días' }**")
            st.caption(estado_mascota)

    st.markdown("<br>", unsafe_allow_html=True)

    # Menú lateral
    st.sidebar.markdown(f"### 👤 Tu Perfil")
    st.sidebar.write(f"🌟 **Nombre:** {st.session_state.nombre_usuario}")
    st.sidebar.write(f"📚 **Carrera:** {st.session_state.carrera_usuario}")
    st.sidebar.write(f"🔥 **Racha:** {st.session_state.racha_dias} días")
    st.sidebar.markdown("---")
    
    # Botón secreto para simular que avanzó un día (Para que puedas probar la mascota tú mismo)
    if st.sidebar.button("🛠️ Simular mañana (Probar Racha)"):
        st.session_state.racha_dias += 1
        st.rerun()
        
    if st.sidebar.button("🚪 Cerrar Sesión / Salir"):
        st.session_state.registrado = False
        st.session_state.nombre_usuario = ""
        st.rerun()

    # Bancos de preguntas específicos por carrera
    banco_preguntas = {
        "Medicina": [
            "1. 📚 ¿Sientes que estudiar materias tan pesadas como anatomía o fisiología te deja sin pila?",
            "2. 💊 ¿Te da pánico o estrés constante no lograr grabarte todos los fármacos o guías clínicas?",
            "3. 🏥 ¿El ritmo tan acelerado y la presión de los hospitales te causa nervios o ansiedad?",
            "4. 🛌 ¿Sientes que tus horas de sueño son un chiste debido a las guardias o entregas?",
            "5. 👑 ¿Te pesa mucho la presión por la jerarquía u opiniones de los doctores adscritos?",
            "6. 🍏 ¿Sientes que por culpa de las clases comes puras tonterías o dejaste el ejercicio?",
            "7. 📉 ¿Te frustra matarte estudiando y sentir que tus notas no reflejan todo ese esfuerzo?",
            "8. 🏔️ ¿Sientes que las exigencias que te ponen en la escuela son una montaña imposible de escalar?",
            "9. 🥊 ¿El ambiente de competencia o 'vibra pesada' entre tus compañeros te estresa?",
            "10. 💔 ¿Sientes que tu carrera te está alejando de tus amigos de siempre o de tu familia?"
        ],
        "Enfermería": [
            "1. 🏃‍♂️ ¿Sientes que tus pies y espalda van a estallar tras pasar tantas horas de pie en el hospital?",
            "2. ❤️ ¿Te cuesta trabajo desconectarte de la carga emocional de cuidar directamente a pacientes graves?",
            "3. 📝 ¿Te abruma sentir que pasas más tiempo llenando hojas y papeleo que atendiendo personas?",
            "4. ⏳ ¿Te da coraje o frustración no tener ni 5 minutos para platicar o atender bien a un paciente?",
            "5. 🔋 ¿Sientes que el hospital te absorbe tanta energía que llegas a casa como un fantasma?",
            "6. 💉 ¿Vives con el miedo constante de equivocarte al preparar o aplicar un medicamento?",
            "7. 🚨 ¿El ambiente del piso o urgencias te hace sentir en un estado de alerta y estrés constante?",
            "8. 🤷‍♂️ ¿Sientes que te matas trabajando en tus prácticas y nadie valora realmente lo que haces?",
            "9. 🥺 ¿Te ha tocado ver casos tan difíciles que te quedas pensando en ellos todo el día?",
            "10. 🛌 ¿Al terminar tu jornada lo único que físicamente puedes hacer es tirarte a la cama?"
        ],
        "Nutrición": [
            "1. 🧮 ¿Te explota la cabeza con tantos cálculos dietéticos, fórmulas y bioquímica por memorizar?",
            "2. 🏁 ¿Sientes que el mundo de la nutrición está tan lleno de gente que da miedo el futuro?",
            "3. 📚 ¿Te estresa sentir que si no lees los últimos artículos te vas a quedar desactualizado?",
            "4. 🗣️ ¿Te agota lidiar con pacientes que quieren soluciones mágicas y no ponen de su parte?",
            "5. 🍽️ ¿Te frustra demasiado cuando preparas un plan hermoso y el paciente no hace nada?",
            "6. 🧪 ¿Sientes que materias ultra pesadas como bioquímica metabólica te están consumiendo la vida?",
            "7. 🧐 ¿Sientes los ojos de tus profesores o asesores encima de ti juzgando cada menú que diseñas?",
            "8. ⏰ ¿Sientes que el día debería tener 30 horas para que te dé tiempo de cumplir con todo?",
            "9. 💼 ¿Te da insomnio pensar si vas a encontrar un buen trabajo o poner consultorio al graduarte?",
            "10. 🍕 ¿Irónicamente el estrés de la carrera ha hecho que descuides tu propia alimentación?"
        ]
    }
    
    preguntas = banco_preguntas.get(
        st.session_state.carrera_usuario, 
        [f"✨ Pregunta {i}: ¿Sientes que la carga académica le quita color y tranquilidad a tus días?" for i in range(1, 11)]
    )
    
    opciones = {
        "😎 ¡Para nada! Nunca me pasa": 0,
        "🙂 A veces me llega a pasar": 2,
        "😥 Sí, me pasa bastante seguido": 4,
        "💥 Definitivamente todos los días": 6
    }
    
    puntos_totales = 0
    
    # Mostrar las preguntas metidas en marcos estéticos
    for i, q in enumerate(preguntas):
        with st.container(border=True):
            seleccion = st.radio(q, list(opciones.keys()), index=0, key=f"p_{i}")
            puntos_totales += opciones[seleccion]

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================================
    # BOTÓN DE RESULTADO 
    # ==========================================
    if st.button("🎯 ¡Analizar mi nivel de Mente Sana!", type="primary", use_container_width=True):
        actualizar_racha() # Registra el día del test para la racha diaria
        max_puntaje = 60
        st.markdown("---")
        st.markdown("<h3 style='text-align: center; color: #1565C0;'>🎯 Tu Diagnóstico Definitivo</h3>", unsafe_allow_html=True)
        
        st.metric(label="Batería de Estrés Acumulada", value=f"{puntos_totales} de {max_puntaje} pts")
        st.markdown("<br>", unsafe_allow_html=True)
        
        if puntos_totales <= 20:
            st.balloons()
            st.success(f"🟢 **¡Estás brillando, {st.session_state.nombre_usuario}! Tu nivel de estrés es Bajo / Saludable.**")
            st.markdown("""
            * **a) Diagnóstico:** ¡Tienes una armadura mental! Estás manejando las presiones de tu carrera como todo un profesional sin dejar que te apaguen.
            * **b) Recomendaciones:** Sigue cuidando tus fines de semana, ríe con tus amigos, come a tus horas y no cambies nada. ¡Vas de diez!
            * **c) Tu frase motivacional:** 
            > *"El éxito no es solo ganar, es mantener tu chispa encendida mientras lo logras."* ✨
            """)
        elif 21 <= puntos_totales <= 40:
            st.warning(f"🟡 **¡Momento de hacer una pausa, {st.session_state.nombre_usuario}! Tu nivel de estrés es Moderado.**")
            st.markdown("""
            * **a) Diagnóstico:** Tu batería está baja. La escuela te está pidiendo mucha energía y estás empezando a trabajar en 'modo ahorro'. Hay que recargar antes de que se complique.
            * **b) Recomendaciones:** Di que no a responsabilidades extra esta semana. Aplica la de estudiar 50 minutos y desconectarte 10 obligatorios para escuchar tu canción favorita o caminar un poco.
            * **c) Tu frase motivacional:** 
            > *"Descansar cuando estás cansado es parte de avanzar. Hasta los mejores guerreros se quitan la armadura para dormir."* 🛡️
            """)
        else:
            st.error(f"🔴 **¡Alerta roja de desgaste, {st.session_state.nombre_usuario}! Tu nivel de estrés es Severo.**")
            st.markdown("""
            * **a) Diagnóstico:** ¡Estás en cortocorticuito! El cansancio se quiere adueñar de ti por completo y estás empujando tu mente mucho más allá de su límite.
            * **b) Recomendaciones urgentes:** Necesitas un día de desconexión total. Habla hoy mismo con alguien de confianza (un amigo, tu familia o un orientador) para desahogarte. Ninguna calificación ni entrega vale más que tu salud física y mental.
            * **c) Tu frase motivacional:** 
            > *"Está bien no poder con todo. Eres un ser humano. Cuidar de ti es tu tarea más importante el día de hoy."* ❤️
            """)
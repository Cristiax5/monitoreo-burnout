import streamlit as st
import random

st.set_page_config(page_title="Mente Sana", page_icon="🧠", layout="centered")

# Estilos CSS
st.markdown("""
    <style>
    .card { background: white; padding: 25px; border-radius: 15px; border: 1px solid #e1e4e8; margin-bottom: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    .stApp { background-color: #f0f2f6; }
    .welcome-text { text-align: center; color: #4a5568; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Estado inicial
if "registrado" not in st.session_state: st.session_state.registrado = False
if "racha" not in st.session_state: st.session_state.racha = 1

# Banco de preguntas (10 preguntas)
banco_preguntas = [
    ("🍎", "¿Sientes que por culpa de las clases comes puras tonterías o dejaste el ejercicio?"),
    ("😴", "¿Tu calidad de sueño se ha visto afectada por la carga académica?"),
    ("⚡", "¿Sientes agotamiento físico al terminar tus jornadas?"),
    ("🧠", "¿Te resulta difícil concentrarte en clase últimamente?"),
    ("💬", "¿Sientes que tu humor ha cambiado negativamente esta semana?"),
    ("⏳", "¿Sientes que el tiempo nunca te alcanza para tus deberes?"),
    ("🔋", "¿Te sientes sin energía al despertar?"),
    ("📚", "¿La carga de estudio te genera ansiedad constante?"),
    ("🤝", "¿Has descuidado tus relaciones personales por el estudio?"),
    ("🧘", "¿Sientes que no tienes momentos de paz durante el día?")
]

# --- INTERFAZ ---
if not st.session_state.registrado:
    st.markdown("<div class='welcome-text'><h1>Bienvenido a Mente Sana 🧠</h1><p>Estamos aquí para acompañarte en tu bienestar día a día.</p></div>", unsafe_allow_html=True)
    nombre = st.text_input("¿Cómo te llamas?")
    carrera = st.selectbox("Selecciona tu carrera:", ["Medicina", "Enfermería", "Nutrición"])
    if st.button("Comenzar mi cuidado diario"):
        st.session_state.registrado = True
        st.session_state.nombre = nombre
        st.rerun()
else:
    # Mascota de Racha
    avatar = "🐣" if st.session_state.racha < 30 else "🦅🔥"
    st.markdown(f"<div style='text-align:center; font-size: 60px;'>{avatar}</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;'><b>Hola {st.session_state.nombre}, llevas una racha de {st.session_state.racha} días cuidando tu mente.</b></p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Encuesta estilo tarjeta
    opciones = {
        "😎 ¡Para nada! Nunca me pasa": 0,
        "🙂 A veces me llega a pasar": 1,
        "😓 Sí, me pasa bastante seguido": 2,
        "💥 Definitivamente todos los días": 3
    }
    
    puntos = 0
    for emoji, texto in banco_preguntas:
        st.markdown(f"<div class='card'>", unsafe_allow_html=True)
        resp = st.radio(f"{emoji} {texto}", list(opciones.keys()))
        puntos += opciones[resp]
        st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Finalizar Análisis"):
        st.session_state.racha += 1
        st.markdown("---")
        
        # Diagnóstico (Sin globos si es negativo)
        if puntos >= 15:
            st.error("⚠️ **Alerta: Tu nivel de estrés requiere atención.**")
            st.write("Es momento de priorizar tu paz. Te recomendamos:")
            st.info("🧘 **Respiración:** Inhala en 4 segundos, mantén 4, exhala en 6.")
            st.info("🚨 **Grounding:** Técnica 5-4-3-2-1 para reconectar con el presente.")
        else:
            st.success("✅ Tu bienestar está en buenos niveles. ¡Sigue así!")
            
        st.info(f"✨ **Frase:** {random.choice(['Eres más que tus deberes.', 'Cuidarte no es un lujo, es una necesidad.', 'Un día a la vez.'])}")
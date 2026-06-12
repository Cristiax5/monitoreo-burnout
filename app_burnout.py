import streamlit as st
import random

# Configuración de página
st.set_page_config(page_title="Mente Sana", page_icon="🧠", layout="centered")

# Estilos CSS
st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #f0f4f8 0%, #d9e2ec 100%); }
    .card { background: white; padding: 25px; border-radius: 20px; border-left: 8px solid #3182ce; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
    .hero { text-align: center; padding: 40px; background: linear-gradient(135deg, #2b6cb0 0%, #4299e1 100%); color: white; border-radius: 25px; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Mascota Evolutiva
def obtener_mascota(racha):
    if racha <= 5: return "🥚", "Huevo Místico"
    elif racha <= 30: return "🐥", "Pollito en crecimiento"
    elif racha <= 60: return "🦆", "Pato Silvestre"
    elif racha <= 90: return "🦉", "Búho de Atenea"
    elif racha <= 120: return "🦅", "Águila Real"
    elif racha < 365: return "🦚", "Pavo Real"
    else: return "🔥", "¡AVE FÉNIX INMORTAL!"

# Inicialización
if "registrado" not in st.session_state: st.session_state.registrado = False
if "racha" not in st.session_state: st.session_state.racha = 1

# --- BARRA LATERAL PROTEGIDA ---
with st.sidebar:
    st.title("⚙️ Panel de Control")
    password = st.text_input("Clave de Administrador:", type="password")
    if password == "Fenix2026":  # Tu clave secreta
        st.success("Modo Edición Activado")
        if st.button("🔥 Evolucionar a Fénix"):
            st.session_state.racha = 366
            st.rerun()
        if st.button("🔄 Resetear Racha"):
            st.session_state.racha = 1
            st.rerun()

# --- BIENVENIDA ---
if not st.session_state.registrado:
    st.markdown("<div class='hero'><h1>¡Hola! Qué gusto verte por aquí. 🧠</h1><p>Esta es tu zona segura para cuidar de tu bienestar mental.</p></div>", unsafe_allow_html=True)
    nombre = st.text_input("¿Cómo te gusta que te llamen?")
    carrera = st.selectbox("¿Qué estudias?", ["Medicina", "Enfermería", "Nutrición"])
    if st.button("Comenzar mi cuidado diario", use_container_width=True):
        if nombre:
            st.session_state.nombre = nombre
            st.session_state.registrado = True
            st.rerun()
        else:
            st.warning("Por favor, dinos cómo prefieres que te llamemos.")
else:
    avatar, etapa = obtener_mascota(st.session_state.racha)
    st.markdown(f"<div style='text-align:center; font-size: 80px;'>{avatar}</div>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center;'>{st.session_state.nombre}, vas en tu {etapa}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;'>Llevas una racha de <b>{st.session_state.racha} días</b> constante. ¡Felicidades!</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    preguntas = [
        ("🍎", "¿Sientes que por culpa de las clases comes puras tonterías o dejaste el ejercicio?"),
        ("😴", "¿Tu calidad de sueño ha sido deficiente esta semana?"),
        ("⚡", "¿Sientes agotamiento físico al terminar tus labores?"),
        ("🧠", "¿La carga mental te impide concentrarte en tus temas personales?"),
        ("💬", "¿Has notado irritabilidad en tu trato con los demás?"),
        ("⏳", "¿Sientes una presión constante por la falta de tiempo?"),
        ("🔋", "¿Sientes que despiertas ya cansado antes de iniciar el día?"),
        ("📚", "¿Te invade la ansiedad al pensar en tus responsabilidades académicas?"),
        ("🤝", "¿Te sientes desconectado de tus amigos o familia?"),
        ("🧘", "¿Sientes que tu mente nunca descansa del estudio?")
    ]
    
    opciones = {"😎 ¡Para nada!": 0, "🙂 A veces": 1, "😓 Sí, seguido": 2, "💥 Definitivamente": 3}
    puntos = 0
    
    for emoji, texto in preguntas:
        st.markdown(f"<div class='card'>", unsafe_allow_html=True)
        resp = st.radio(f"{emoji} {texto}", list(opciones.keys()))
        puntos += opciones[resp]
        st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Finalizar Análisis", use_container_width=True):
        st.session_state.racha += 1
        st.markdown("---")
        if puntos >= 15:
            st.error("⚠️ **Diagnóstico: Alerta de Estrés**")
            st.info("🌬️ **Respiración 4-7-8:** Inhala 4s, mantén 7s, exhala 8s.")
            st.info("🌍 **Técnica 5-4-3-2-1:** Reconecta con tus sentidos.")
        else:
            st.success("✅ ¡Equilibrio emocional estable!")
        st.info(f"✨ **Frase:** '{random.choice(['Eres más que tus calificaciones.', 'La constancia es la llave.', 'Cuidar de ti es tu mayor éxito.'])}'")
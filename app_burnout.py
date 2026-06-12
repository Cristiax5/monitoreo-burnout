import streamlit as st
import random

# Configuración de página
st.set_page_config(page_title="Mente Sana", page_icon="🧠", layout="centered")

# Estilos CSS más cálidos y amigables
st.markdown("""
    <style>
    .stApp { background-color: #fdfcf9; }
    .hero { text-align: center; padding: 40px; background: #eef2f3; border-radius: 30px; color: #2d3748; margin-bottom: 30px; }
    .card { background: #ffffff; padding: 25px; border-radius: 25px; border: 1px solid #edf2f7; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
    .stButton>button { border-radius: 50px !important; background-color: #63b3ed !important; color: white !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# Lógica de Evolución Progresiva (Día a día)
def obtener_mascota(racha):
    if racha <= 5: return "🥚", "Huevo Místico"
    elif racha <= 30: return "🐥", "Pollito Bebé"
    elif racha <= 60: return "🦆", "Pato Silvestre"
    elif racha <= 90: return "🦉", "Búho Sabio"
    elif racha <= 120: return "🦅", "Águila Real"
    elif racha < 365: return "🦚", "Pavo Real Majestuoso"
    else: return "🔥", "¡AVE FÉNIX INMORTAL!"

# Inicialización
if "registrado" not in st.session_state: st.session_state.registrado = False
if "racha" not in st.session_state: st.session_state.racha = 1

# --- PANEL DE ADMINISTRACIÓN (Oculto para presentación) ---
with st.sidebar:
    st.write("---")
    if st.text_input("Clave Admin", type="password") == "Fenix2026":
        if st.button("Avanzar 1 día"): st.session_state.racha += 1; st.rerun()

# --- BIENVENIDA ---
if not st.session_state.registrado:
    st.markdown("<div class='hero'><h1>¡Hola! Es un gusto verte. 🌿</h1><p>Estamos listos para cuidar de tu bienestar mental hoy.</p></div>", unsafe_allow_html=True)
    nombre = st.text_input("¿Cómo te gusta que te llamen?")
    if st.button("Comenzar mi cuidado diario"):
        if nombre:
            st.session_state.nombre = nombre
            st.session_state.registrado = True
            st.rerun()
else:
    avatar, etapa = obtener_mascota(st.session_state.racha)
    st.markdown(f"<div style='text-align:center; font-size: 90px;'>{avatar}</div>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center; color: #4a5568;'>{st.session_state.nombre}, vas en tu {etapa}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;'>Día de racha: <b>{st.session_state.racha}</b>. ¡Cada día es un paso adelante!</p>", unsafe_allow_html=True)
    
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
    
    puntos = 0
    for emoji, texto in preguntas:
        st.markdown(f"<div class='card'>", unsafe_allow_html=True)
        resp = st.radio(f"{emoji} {texto}", ["😎 ¡Para nada!", "🙂 A veces", "😓 Sí, seguido", "💥 Definitivamente"], horizontal=True)
        valores = {"😎 ¡Para nada!": 0, "🙂 A veces": 1, "😓 Sí, seguido": 2, "💥 Definitivamente": 3}
        puntos += valores[resp]
        st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Finalizar Análisis"):
        st.session_state.racha += 1 # Evolución progresiva diaria
        st.markdown("---")
        if puntos >= 15:
            st.error("⚠️ **Diagnóstico de atención**")
            st.write("Has tenido días pesados. Por favor, intenta:")
            st.info("🌬️ **Respiración 4-7-8:** Inhala 4s, mantén 7s, exhala 8s.")
            st.info("🌍 **Técnica 5-4-3-2-1:** Reconecta con tu entorno físico.")
        else:
            st.success("✅ ¡Qué bien! Tu estado emocional es equilibrado.")
        st.info(f"✨ **Frase:** '{random.choice(['Eres más que tus deberes.', 'La constancia es la llave.', 'Cuidar de ti es tu mayor éxito.'])}'")
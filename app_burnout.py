import streamlit as st
import random

st.set_page_config(page_title="Mente Sana", page_icon="🧠", layout="centered")

# Estilos CSS para el formato de tarjetas idéntico a tu imagen
st.markdown("""
    <style>
    .card { background: white; padding: 25px; border-radius: 15px; border: 1px solid #e1e4e8; margin-bottom: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    .stApp { background-color: #f0f2f6; }
    h1 { text-align: center; color: #1f2937; }
    </style>
    """, unsafe_allow_html=True)

# Estado
if "carrera" not in st.session_state: st.session_state.carrera = None

# --- BANCO DE PREGUNTAS (Formato idéntico a la imagen) ---
banco = {
    "Medicina": [
        ("🍎", "¿Sientes que por culpa de las clases comes puras tonterías o dejaste el ejercicio?"),
        ("😴", "¿Tu calidad de sueño se ha visto afectada por la carga académica?"),
        ("⚡", "¿Sientes agotamiento físico al terminar tus guardias o clases?")
    ]
}

# --- INTERFAZ ---
if st.session_state.carrera is None:
    st.title("🧠 Mente Sana")
    st.session_state.carrera = st.selectbox("Selecciona tu carrera:", ["Medicina", "Enfermería", "Nutrición"])
    if st.button("Comenzar Evaluación"): st.rerun()
else:
    st.title("Evaluación Diaria")
    
    opciones = {
        "😎 ¡Para nada! Nunca me pasa": 0,
        "🙂 A veces me llega a pasar": 1,
        "😓 Sí, me pasa bastante seguido": 2,
        "💥 Definitivamente todos los días": 3
    }
    
    puntos_totales = 0
    # Generar preguntas visuales tipo tarjeta
    for emoji, texto in banco["Medicina"]: # Puedes extender esto a otras carreras
        st.markdown(f"<div class='card'>", unsafe_allow_html=True)
        resp = st.radio(f"{emoji} {texto}", list(opciones.keys()))
        puntos_totales += opciones[resp]
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Finalizar y diagnosticar"):
        st.markdown("---")
        if puntos_totales >= 4:
            st.error("⚠️ **Alerta: Nivel de estrés detectado**")
            st.write("Tu salud es prioridad. Te recomendamos:")
            st.info("🧘 **Respiración:** Inhala en 4 segundos, mantén 4, exhala en 6.")
            st.info("🚨 **Grounding:** Técnica 5-4-3-2-1 (Identifica 5 cosas que veas, 4 que toques, 3 que oigas, 2 que huelas y 1 que pruebes).")
        else:
            st.success("✅ Tu nivel de estrés se mantiene en rangos controlados.")
            st.write("Mantén tus hábitos saludables, ¡vas muy bien!")
            
        st.markdown(f"**Frase del día:** {random.choice(['Cuidarte es tu mayor responsabilidad.', 'Un paso a la vez.', 'No estás solo en este proceso.'])}")
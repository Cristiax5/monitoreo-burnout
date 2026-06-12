import streamlit as st
import random

# Configuración visual
st.set_page_config(page_title="Mente Sana", page_icon="🧠", layout="centered")

# Estilos CSS personalizados para tarjetas elegantes
st.markdown("""
    <style>
    .stApp { background-color: #f5f7f9; }
    .card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Inicialización
if "registrado" not in st.session_state: st.session_state.registrado = False
if "racha_dias" not in st.session_state: st.session_state.racha_dias = 1
if "inventario" not in st.session_state:
    st.session_state.inventario = {"🍏 Manzana Dorada": 1, "💡 Lámpara de Incubación": 1, "🌾 Semillas de la Calma": 2}
if "accion_mascota" not in st.session_state: st.session_state.accion_mascota = "¡Hola! Estoy listo para cuidar tu mente."

def obtener_sistema_mascota(racha):
    if racha <= 5: return "🥚", "Fase: Huevo Místico"
    elif racha <= 30: return "🐥", "Fase: Pollito Bebé"
    elif racha <= 60: return "🦆", "Fase: Pato Silvestre"
    elif racha <= 90: return "🦉", "Fase: Búho de Atenea"
    elif racha <= 120: return "🦅", "Fase: Águila Real"
    elif racha < 365: return "🦚", "Fase: Pavo Real"
    else: return "🦅🔥", "Fase: ¡AVE FÉNIX INMORTAL!"

# --- INTERFAZ ---
if not st.session_state.registrado:
    st.markdown("<h1 style='text-align: center; color: #2c3e50;'>🧠 Mente Sana</h1>", unsafe_allow_html=True)
    with st.container():
        st.session_state.nombre_usuario = st.text_input("Tu nombre:")
        st.session_state.carrera_usuario = st.selectbox("Carrera:", ["Medicina", "Enfermería", "Nutrición"])
        if st.button("Comenzar Viaje", use_container_width=True):
            st.session_state.registrado = True
            st.rerun()
else:
    avatar, fase = obtener_sistema_mascota(st.session_state.racha_dias)
    
    # Header elegante
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(f"<div class='card' style='text-align:center; font-size:50px;'>{avatar}</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"### {st.session_state.nombre_usuario}")
        st.write(f"**Racha:** {st.session_state.racha_dias} días | **{fase}**")
        st.info(f"💬 {st.session_state.accion_mascota}")

    # Interacciones rápidas
    c1, c2 = st.columns(2)
    if c1.button("👋 Acariciar"): st.session_state.accion_mascota = "¡Tu mascota se siente muy querida! 💕"
    if c2.button("🎶 Cantar"): st.session_state.accion_mascota = "¡Hicieron un dúo hermoso! 🎵"

    # Inventario
    with st.expander("🎒 Mochila de Recompensas"):
        for item, cant in st.session_state.inventario.items():
            if st.button(f"Usar {item} (Tiene {cant})", use_container_width=True):
                if cant > 0:
                    st.session_state.inventario[item] -= 1
                    st.session_state.accion_mascota = f"¡Usaste {item}! La mascota está feliz."
                    st.rerun()

    # Cuestionario profesional
    st.markdown("---")
    st.markdown("### 📝 Check-in Diario")
    opciones = {"A) Nunca": 0, "B) A veces": 2, "C) Seguido": 4, "D) Siempre": 6}
    
    puntos = 0
    preguntas = ["¿Te sientes agotado hoy?", "¿La carga de trabajo es excesiva?", "¿Dormiste bien?"]
    
    for i, q in enumerate(preguntas):
        st.write(f"**{i+1}. {q}**")
        puntos += opciones[st.radio(f"q{i}", list(opciones.keys()), key=f"q{i}", label_visibility="collapsed")]

    if st.button("🎯 Finalizar Check-in", use_container_width=True):
        st.session_state.racha_dias += 1
        st.success("¡Análisis guardado con éxito!")
        st.rerun()

    # Barra lateral
    st.sidebar.button("🔥 Saltar al Fénix (Día 365)", on_click=lambda: setattr(st.session_state, 'racha_dias', 365))
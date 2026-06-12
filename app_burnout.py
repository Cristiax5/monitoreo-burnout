import streamlit as st
import random

# Configuración de página estilo "App Móvil"
st.set_page_config(page_title="Mente Sana", page_icon="🧠", layout="centered")

# CSS para el estilo estilo TikTok / App moderna
st.markdown("""
    <style>
    @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-15px); } 100% { transform: translateY(0px); } }
    .mascota-animada { animation: float 3s ease-in-out infinite; font-size: 100px; text-align: center; margin-bottom: 20px; }
    .stApp { background: linear-gradient(180deg, #f0f2f5 0%, #ffffff 100%); }
    .stButton>button { border-radius: 20px; border: none; background-color: #fe2c55; color: white; font-weight: bold; }
    .stButton>button:hover { background-color: #e6234a; }
    </style>
    """, unsafe_allow_html=True)

# Estado inicial
if "registrado" not in st.session_state: st.session_state.registrado = False
if "racha_dias" not in st.session_state: st.session_state.racha_dias = 1
if "inventario" not in st.session_state: st.session_state.inventario = {"🍏 Manzana": 2, "💡 Lámpara": 1}
if "accion" not in st.session_state: st.session_state.accion = "¡Hola! Estoy listo para crecer contigo."

def obtener_mascota(racha):
    if racha <= 5: return "🥚", "Fase: Huevo Místico"
    elif racha <= 30: return "🐥", "Fase: Pollito Bebé"
    elif racha <= 60: return "🦆", "Fase: Pato Silvestre"
    elif racha <= 90: return "🦉", "Fase: Búho de Atenea"
    elif racha <= 120: return "🦅", "Fase: Águila Real"
    elif racha < 365: return "🦚", "Fase: Pavo Real"
    else: return "🦅🔥", "Fase: ¡AVE FÉNIX INMORTAL!"

# --- INTERFAZ ---
if not st.session_state.registrado:
    st.markdown("<h1 style='text-align: center;'>🧠 Mente Sana</h1>", unsafe_allow_html=True)
    st.session_state.nombre = st.text_input("¿Cómo te llamas?")
    if st.button("🚀 Entrar"):
        st.session_state.registrado = True
        st.rerun()
else:
    avatar, fase = obtener_mascota(st.session_state.racha_dias)
    
    # Mascota flotante estilo TikTok
    st.markdown(f"<div class='mascota-animada'>{avatar}</div>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center;'>{fase}</h3>", unsafe_allow_html=True)
    st.success(st.session_state.accion)
    
    # Interacciones rápidas
    col1, col2 = st.columns(2)
    if col1.button("💕 Acariciar"): st.session_state.accion = "¡Tu mascota está flotando de felicidad! ✨"
    if col2.button("🎶 Cantar"): st.session_state.accion = "¡Qué dueto tan hermoso! 🎵"

    # Inventario
    with st.expander("🎒 Mochila"):
        for item, cant in st.session_state.inventario.items():
            if st.button(f"Usar {item} ({cant})"):
                st.session_state.accion = f"¡Alimentaste a tu mascota con {item}! Es más fuerte ahora."
                st.rerun()

    # Evaluación (10 preguntas)
    st.markdown("---")
    st.subheader("📝 Check-in Diario (10 pts)")
    puntos = 0
    for i in range(10):
        val = st.radio(f"Pregunta {i+1}: ¿Cómo te sientes?", ["Nunca", "A veces", "Seguido", "Siempre"], horizontal=True, key=f"q{i}")
        puntos += {"Nunca":0, "A veces":1, "Seguido":2, "Siempre":3}[val]

    if st.button("✅ Enviar Diagnóstico"):
        st.session_state.racha_dias += 1
        st.balloons()
        # Diagnóstico clínico simple
        if puntos < 10: st.success("¡Mentalidad brillante! Todo bajo control.")
        elif puntos < 20: st.warning("Nivel moderado: Tómate un respiro hoy.")
        else: st.error("¡Cuidado! Tu nivel de estrés es alto, descansa.")
        
        # Premio
        premio = random.choice(list(st.session_state.inventario.keys()))
        st.session_state.inventario[premio] = st.session_state.inventario.get(premio, 0) + 1
        st.rerun()

    if st.sidebar.button("🔥 Saltar al Fénix"):
        st.session_state.racha_dias = 365
        st.rerun()
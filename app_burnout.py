import streamlit as st
import random

st.set_page_config(page_title="Mente Sana", page_icon="🧠", layout="centered")

# CSS para movimiento y estilo TikTok
st.markdown("""
    <style>
    @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-15px); } 100% { transform: translateY(0px); } }
    .mascota-animada { animation: float 3s ease-in-out infinite; font-size: 100px; text-align: center; }
    .stButton>button { border-radius: 20px; background-color: #fe2c55; color: white; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# Función JavaScript para que la mascota "hable" (haga sonidos)
def emitir_sonido(mensaje):
    js_code = f"""
    <script>
        var msg = new SpeechSynthesisUtterance("{mensaje}");
        msg.pitch = 1.5; // Tono agudo para ave
        msg.rate = 1.2;
        window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js_code, height=0)

# Estado
if "registrado" not in st.session_state: st.session_state.registrado = False
if "racha_dias" not in st.session_state: st.session_state.racha_dias = 1
if "inventario" not in st.session_state: st.session_state.inventario = {"Manzana": 1}

def obtener_mascota(racha):
    if racha <= 5: return "🥚", "Huevo Místico"
    elif racha < 365: return "🐥", "Pollito en crecimiento"
    else: return "🦅🔥", "¡AVE FÉNIX INMORTAL!"

# --- INTERFAZ ---
if not st.session_state.registrado:
    st.markdown("<h1>🧠 Mente Sana</h1>", unsafe_allow_html=True)
    st.session_state.nombre = st.text_input("Tu nombre:")
    if st.button("🚀 Entrar"):
        st.session_state.registrado = True
        st.rerun()
else:
    avatar, fase = obtener_mascota(st.session_state.racha_dias)
    st.markdown(f"<div class='mascota-animada'>{avatar}</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    if col1.button("💕 Acariciar"): 
        emitir_sonido("¡Pío pío! Me haces muy feliz")
    if col2.button("🎶 Cantar"): 
        emitir_sonido("¡Trino trino! ¡Qué hermosa melodía!")

    st.markdown("---")
    st.subheader("📝 Check-in Diario")
    puntos = 0
    preguntas = [f"Pregunta {i+1}" for i in range(10)]
    for i, q in enumerate(preguntas):
        res = st.radio(f"{q}: ¿Cómo te sientes?", ["Nunca", "A veces", "Seguido", "Siempre"], horizontal=True, key=f"q{i}")
        puntos += {"Nunca": 0, "A veces": 2, "Seguido": 4, "Siempre": 6}[res]

    if st.button("✅ Analizar Diagnóstico"):
        st.session_state.racha_dias += 1
        st.balloons()
        
        # Diagnóstico al final
        st.subheader("📊 Tu Diagnóstico Clínico")
        if puntos <= 15:
            st.success(f"Puntaje {puntos}: ¡Excelente! Tu salud mental es sólida. Tu ave está orgullosa.")
        elif puntos <= 35:
            st.warning(f"Puntaje {puntos}: Nivel Moderado. Toma un respiro, tu mascota te necesita tranquilo.")
        else:
            st.error(f"Puntaje {puntos}: Alerta. Prioriza tu descanso, tu salud es prioridad.")
            
        emitir_sonido("Análisis completado. Por favor, cuídate mucho.")

    if st.sidebar.button("🔥 Saltar al Fénix"):
        st.session_state.racha_dias = 365
        st.rerun()
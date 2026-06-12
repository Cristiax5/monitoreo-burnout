import streamlit as st
import random

# Configuración de página
st.set_page_config(page_title="Mente Sana", page_icon="🧠", layout="centered")

# CSS para movimiento y estilo TikTok
st.markdown("""
    <style>
    @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-15px); } 100% { transform: translateY(0px); } }
    .mascota-animada { animation: float 3s ease-in-out infinite; font-size: 100px; text-align: center; }
    .stButton>button { border-radius: 20px; background-color: #fe2c55; color: white; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# Función de sonido con JavaScript (Sonidos de ave)
def reproducir_sonido(tipo):
    sonidos = {
        "acariciar": "Pio pio, me haces feliz",
        "cantar": "Trino trino, qué hermosa melodía",
        "manzana": "Ñam ñam, gracias por la fruta",
        "lampara": "Qué calientito, me siento seguro",
        "semillas": "Gracias por la calma, me siento en paz",
        "diagnostico": "Análisis completado, por favor cuídate mucho"
    }
    texto = sonidos.get(tipo, "Pio")
    js_code = f"""
    <script>
        var msg = new SpeechSynthesisUtterance("{texto}");
        msg.pitch = 2.0; msg.rate = 1.3;
        window.speechSynthesis.speak(msg);
    </script>
    """
    st.components.v1.html(js_code, height=0)

# Estado inicial
if "registrado" not in st.session_state: st.session_state.registrado = False
if "racha_dias" not in st.session_state: st.session_state.racha_dias = 1
if "inventario" not in st.session_state: st.session_state.inventario = {"Manzana": 1, "Lámpara": 1, "Semillas": 1}

def obtener_mascota(racha):
    if racha <= 5: return "🥚", "Huevo Místico"
    elif racha < 365: return "🐥", "Pollito en crecimiento"
    else: return "🦅🔥", "¡AVE FÉNIX INMORTAL!"

# --- INTERFAZ ---
if not st.session_state.registrado:
    st.markdown("<h1>🧠 Mente Sana</h1>", unsafe_allow_html=True)
    st.session_state.nombre = st.text_input("Nombre:")
    if st.button("🚀 Entrar"): st.session_state.registrado = True; st.rerun()
else:
    avatar, fase = obtener_mascota(st.session_state.racha_dias)
    st.markdown(f"<div class='mascota-animada'>{avatar}</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    if col1.button("💕 Acariciar"): reproducir_sonido("acariciar")
    if col2.button("🎶 Cantar"): reproducir_sonido("cantar")

    with st.expander("🎒 Mochila"):
        for item in list(st.session_state.inventario.keys()):
            if st.button(f"Usar {item}"): reproducir_sonido(item.lower())

    st.markdown("---")
    st.subheader("📝 Evaluación Biopsicosocial")
    puntos = 0
    preguntas = [f"Pregunta {i+1}" for i in range(10)]
    for i, q in enumerate(preguntas):
        res = st.radio(f"{q}: ¿Cómo te sientes?", ["Nunca", "A veces", "Seguido", "Siempre"], horizontal=True, key=f"q{i}")
        puntos += {"Nunca": 0, "A veces": 2, "Seguido": 4, "Siempre": 6}[res]

    if st.button("✅ Finalizar Análisis"):
        st.session_state.racha_dias += 1
        st.balloons()
        reproducir_sonido("diagnostico")
        
        st.subheader("📊 Tu Diagnóstico y Recomendaciones")
        if puntos <= 15:
            st.success(f"Puntaje {puntos}: ¡Excelente! Tu salud mental es sólida.")
            st.write("💡 **Consejo:** Mantén este equilibrio, tu rutina es muy saludable.")
        elif puntos <= 35:
            st.warning(f"Puntaje {puntos}: Nivel Moderado. Necesitas una pausa.")
            st.write("🧘 **Recomendación:** Practica la respiración diafragmática 3 minutos: inhala en 4, mantén en 4, exhala en 6.")
        else:
            st.error(f"Puntaje {puntos}: Nivel de Alerta. Tu salud es prioridad.")
            st.write("🚨 **Acción:** Apaga todo, hidrátate y realiza una técnica de grounding 5-4-3-2-1.")
            
        frases = ["¡Eres más fuerte de lo que crees!", "Cada día es una nueva oportunidad.", "Tu esfuerzo vale cada segundo."]
        st.info(f"✨ **Frase del día:** {random.choice(frases)}")

    if st.sidebar.button("🔥 Saltar al Fénix"): st.session_state.racha_dias = 365; st.rerun()
import streamlit as st
import random

# Configuración visual con animación de flotación
st.set_page_config(page_title="Mente Sana", page_icon="🧠", layout="centered")

st.markdown("""
    <style>
    @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-20px); } 100% { transform: translateY(0px); } }
    .mascota-animada { animation: float 3s ease-in-out infinite; font-size: 80px; text-align: center; }
    .hero-card { background: linear-gradient(135deg, #1e88e5 0%, #1565c0 100%); color: white; padding: 40px; border-radius: 25px; text-align: center; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# Estado inicial
if "registrado" not in st.session_state: st.session_state.registrado = False
if "racha_dias" not in st.session_state: st.session_state.racha_dias = 1
if "accion" not in st.session_state: st.session_state.accion = "¡Hola! Estoy esperando tu cariño."
if "inventario" not in st.session_state: st.session_state.inventario = {"Manzana": 1, "Lámpara": 1, "Semillas": 2}

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
    st.markdown("<div class='hero-card'><h1>🧠 Mente Sana</h1><p>Evaluación de salud mental para alto rendimiento.</p></div>", unsafe_allow_html=True)
    st.session_state.nombre = st.text_input("Tu nombre:")
    st.session_state.carrera = st.selectbox("Carrera:", ["Medicina", "Enfermería", "Nutrición"])
    if st.button("🚀 Iniciar"):
        st.session_state.registrado = True
        st.rerun()
else:
    avatar, fase = obtener_mascota(st.session_state.racha_dias)
    st.markdown(f"<div class='mascota-animada'>{avatar}</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:center;'><b>{fase} | Racha: {st.session_state.racha_dias} días</b></p>", unsafe_allow_html=True)
    st.info(f"💬 {st.session_state.accion}")
    
    # Check-in 10 preguntas
    st.markdown("---")
    st.subheader("📝 Evaluación Diaria (10 preguntas)")
    puntos = 0
    preguntas = [
        "¿Te sientes agotado hoy?", "¿La carga de estudio es excesiva?", 
        "¿Has dormido bien esta semana?", "¿Te sientes motivado?",
        "¿Sientes presión por tus superiores?", "¿Tu alimentación es equilibrada?",
        "¿Tienes tiempo para hobbies?", "¿La jerarquía te genera estrés?",
        "¿Te sientes valorado?", "¿Tu salud mental es prioridad hoy?"
    ]
    
    for i, q in enumerate(preguntas):
        res = st.radio(f"{i+1}. {q}", ["Nunca", "A veces", "Seguido", "Siempre"], horizontal=True, key=f"q{i}")
        valores = {"Nunca": 0, "A veces": 2, "Seguido": 4, "Siempre": 6}
        puntos += valores[res]
    
    if st.button("✅ Finalizar Análisis"):
        st.session_state.racha_dias += 1
        
        # --- DIAGNÓSTICO FINAL ---
        st.markdown("---")
        st.subheader("📊 Resultado del Diagnóstico")
        if puntos <= 15:
            st.success(f"Puntaje {puntos}: ¡Excelente! Tu salud mental es sólida.")
        elif puntos <= 35:
            st.warning(f"Puntaje {puntos}: Nivel Moderado. Toma un descanso hoy.")
        else:
            st.error(f"Puntaje {puntos}: Nivel de Alerta. Prioriza tu descanso, ¡eres importante!")
        
        # Premio
        premio = random.choice(list(st.session_state.inventario.keys()))
        st.session_state.inventario[premio] += 1
        st.balloons()
        st.write(f"🎁 ¡Has ganado una **{premio}** para tu mascota!")
        
        if st.button("Volver al inicio"): st.rerun()

    if st.sidebar.button("🔥 Saltar al Fénix"):
        st.session_state.racha_dias = 365
        st.rerun()
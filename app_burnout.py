import streamlit as st
import random

st.set_page_config(page_title="Mente Sana", page_icon="🧠", layout="centered")

# CSS estilo TikTok y Animación
st.markdown("""
    <style>
    @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-15px); } 100% { transform: translateY(0px); } }
    .mascota-animada { animation: float 3s ease-in-out infinite; font-size: 100px; text-align: center; }
    .stButton>button { border-radius: 20px; background-color: #fe2c55; color: white; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# Sonidos de Ave (Trinos cortos y rápidos)
def emitir_trino():
    js_code = """
    <script>
        var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        function playTrino(freq, time) {
            var osc = audioCtx.createOscillator();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(freq, audioCtx.currentTime + time);
            osc.connect(audioCtx.destination);
            osc.start(audioCtx.currentTime + time);
            osc.stop(audioCtx.currentTime + time + 0.1);
        }
        playTrino(1000, 0); playTrino(1200, 0.1); playTrino(1000, 0.2);
    </script>
    """
    st.components.v1.html(js_code, height=0)

# Inicialización
if "registrado" not in st.session_state: st.session_state.registrado = False
if "racha_dias" not in st.session_state: st.session_state.racha_dias = 1

# Banco de preguntas con respuestas clínicas coherentes
def obtener_contenido(carrera, racha):
    bancos = {
        "Medicina": ["¿Presentas agotamiento post-guardia?", "¿Tu carga de pacientes sobrepasa tu capacidad?", "¿Sientes estrés por errores clínicos?", "¿La jerarquía hospitalaria afecta tu ánimo?", "¿Tienes tiempo para tu vida personal?", "¿El estudio constante te genera ansiedad?", "¿Logras desconectarte al llegar a casa?", "¿Sientes satisfacción en tu labor?", "¿Tu equipo de trabajo es solidario?", "¿Has dormido menos de 6 horas?"],
        "Enfermería": ["¿Sientes dolor físico por la jornada?", "¿La carga emocional de los pacientes te afecta?", "¿Sientes que el equipo no colabora?", "¿Tienes tiempo para comer bien?", "¿El papeleo excede tu tiempo real?", "¿Sientes estrés por turnos rotativos?", "¿Tu ambiente laboral es tenso?", "¿Sientes fatiga mental crónica?", "¿Te sientes valorado por el sistema?", "¿Tu sueño ha sido reparador?"],
        "Nutrición": ["¿El volumen de consultas te genera estrés?", "¿Sientes presión por los resultados de pacientes?", "¿Te sientes actualizado en tu campo?", "¿Tu dieta personal es descuidada?", "¿El entorno laboral es competitivo?", "¿Sientes frustración por adherencia de pacientes?", "¿Tienes tiempo para actividad física?", "¿La carga administrativa es alta?", "¿Te sientes seguro en tus diagnósticos?", "¿Sientes presión docente o académica?"]
    }
    random.seed(racha)
    preguntas = random.sample(bancos.get(carrera, bancos["Medicina"]), 10)
    # Respuesta coherente con la frecuencia/intensidad
    opciones = {"Nunca": 0, "Rara vez": 1, "Frecuentemente": 2, "Casi siempre": 3}
    return preguntas, opciones

# --- INTERFAZ ---
if not st.session_state.registrado:
    st.markdown("<h1>🧠 Mente Sana</h1>", unsafe_allow_html=True)
    st.session_state.nombre = st.text_input("Nombre:")
    st.session_state.carrera = st.selectbox("Selecciona tu carrera:", ["Medicina", "Enfermería", "Nutrición"])
    if st.button("🚀 Entrar"): st.session_state.registrado = True; st.rerun()
else:
    avatar = "🐣" if st.session_state.racha_dias < 30 else "🦅🔥"
    st.markdown(f"<div class='mascota-animada'>{avatar}</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    if col1.button("💕 Acariciar"): emitir_trino()
    if col2.button("🎶 Cantar"): emitir_trino()

    st.markdown("---")
    preguntas, opciones = obtener_contenido(st.session_state.carrera, st.session_state.racha_dias)
    puntos = 0
    for i, q in enumerate(preguntas):
        res = st.radio(f"{i+1}. {q}", list(opciones.keys()), horizontal=True, key=f"q{i}")
        puntos += opciones[res]

    if st.button("✅ Finalizar Análisis"):
        st.session_state.racha_dias += 1
        st.balloons()
        
        st.subheader("📊 Diagnóstico Clínico")
        if puntos <= 10: st.success("Estado: Saludable. ¡Continúa así!")
        elif puntos <= 20: 
            st.warning("Estado: Riesgo Moderado.")
            st.write("🧘 **Recomendación:** Técnica 4-7-8 (Inhala 4, retén 7, exhala 8).")
        else: 
            st.error("Estado: Alerta. Busca apoyo profesional.")
            st.write("🚨 **Acción:** Ejercicio 5-4-3-2-1 para Grounding mental.")
            
        st.info(f"✨ Frase: {random.choice(['Eres vital para el sistema.', 'Descansa hoy para brillar mañana.', 'Tu bienestar es la medicina principal.'])}")
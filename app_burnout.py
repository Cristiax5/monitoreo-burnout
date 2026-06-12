import streamlit as st
import random

st.set_page_config(page_title="Mente Sana", page_icon="🧠", layout="centered")

st.markdown("""
    <style>
    @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-15px); } 100% { transform: translateY(0px); } }
    .mascota-animada { animation: float 3s ease-in-out infinite; font-size: 100px; text-align: center; }
    .stButton>button { border-radius: 20px; background-color: #fe2c55; color: white; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# Sonido de ave (Más agudo y rápido)
def emitir_trino():
    js_code = """
    <script>
        var ctx = new (window.AudioContext || window.webkitAudioContext)();
        function nota(f, t) {
            var o = ctx.createOscillator();
            o.type = 'square'; o.frequency.setValueAtTime(f, t);
            o.connect(ctx.destination); o.start(t); o.stop(t + 0.05);
        }
        nota(1500, ctx.currentTime); nota(2000, ctx.currentTime + 0.05);
    </script>
    """
    st.components.v1.html(js_code, height=0)

if "registrado" not in st.session_state: st.session_state.registrado = False
if "racha_dias" not in st.session_state: st.session_state.racha_dias = 1

def obtener_mascota(racha):
    if racha <= 5: return "🥚", "Fase: Huevo Místico"
    elif racha < 365: return "🐥", "Fase: Pollito en crecimiento"
    else: return "🦅🔥", "¡AVE FÉNIX INMORTAL!"

# Banco extendido (20 preguntas por carrera)
bancos = {
    "Medicina": ["¿Lograste descansar?", "¿El estrés clínico pesa?", "¿Comiste bien?", "¿Te sientes actualizado?", "¿La jerarquía te afecta?", "¿Dormiste guardias?", "¿Tu salud mental es prioridad?", "¿Tienes tiempo social?", "¿El ritmo es muy rápido?", "¿Te frustra el estudio?", "¿Sientes carga por pacientes graves?", "¿El entorno hospitalario es hostil?", "¿Te sientes físicamente agotado?", "¿Tu memoria falla?", "¿Sientes falta de apoyo?", "¿Te preocupan los errores?", "¿Sientes despersonalización?", "¿Te falta tiempo de ocio?", "¿Tu sueño es interrumpido?", "¿Sientes satisfacción vocacional?"],
    "Enfermería": ["¿Sientes dolor de espalda?", "¿La carga emocional es alta?", "¿El papeleo te abruma?", "¿Tienes energía física?", "¿El ambiente es caótico?", "¿Te sientes valorado?", "¿Has comido hoy?", "¿Tu sueño es reparador?", "¿El hospital te drena?", "¿Te sientes satisfecho?", "¿Mucho trato con familiares?", "¿Sientes falta de insumos?", "¿El turno fue estresante?", "¿Sientes sobrecarga laboral?", "¿Hay buena comunicación?", "¿Te sientes agotado?", "¿La presión es constante?", "¿Tienes apoyo familiar?", "¿Te sientes seguro en el área?", "¿Hay mucha rotación?"],
    "Nutrición": ["¿Cálculos difíciles hoy?", "¿Pacientes que no siguen planes?", "¿Te sientes actualizado?", "¿Mucho estrés metabólico?", "¿Tu dieta está descuidada?", "¿Te frustra el paciente?", "¿Sientes presión docente?", "¿Tienes tiempo personal?", "¿Te sientes seguro?", "¿Mucho estudio hoy?", "¿Dificultad en consultas?", "¿Sientes fatiga mental?", "¿Logras tus metas diarias?", "¿El paciente colabora?", "¿Te falta organización?", "¿Sientes mucha carga teórica?", "¿El ambiente es profesional?", "¿Hay apoyo en el centro?", "¿Te sientes motivado?", "¿Tienes buena técnica?"]
}

if not st.session_state.registrado:
    st.markdown("<h1>🧠 Mente Sana</h1>", unsafe_allow_html=True)
    st.session_state.nombre = st.text_input("Nombre:")
    st.session_state.carrera = st.selectbox("Carrera:", ["Medicina", "Enfermería", "Nutrición"])
    if st.button("🚀 Entrar"): st.session_state.registrado = True; st.rerun()
else:
    avatar, fase = obtener_mascota(st.session_state.racha_dias)
    st.markdown(f"<div class='mascota-animada'>{avatar}</div>", unsafe_allow_html=True)
    st.write(f"**{fase}**")
    
    col1, col2 = st.columns(2)
    if col1.button("💕 Acariciar"): emitir_trino()
    if col2.button("🎶 Cantar"): emitir_trino()

    st.markdown("---")
    random.seed(st.session_state.racha_dias)
    preguntas = random.sample(bancos[st.session_state.carrera], 10)
    puntos = 0
    for i, q in enumerate(preguntas):
        res = st.radio(f"{i+1}. {q}", ["Nunca", "Rara vez", "Frecuentemente", "Casi siempre"], horizontal=True)
        puntos += {"Nunca": 0, "Rara vez": 1, "Frecuentemente": 2, "Casi siempre": 3}[res]

    if st.button("✅ Finalizar Análisis"):
        st.session_state.racha_dias += 1
        st.balloons()
        st.subheader("📊 Diagnóstico Clínico")
        if puntos <= 10: st.success("Estado: Saludable. ¡Tu ave brilla de felicidad!")
        elif puntos <= 20: 
            st.warning("Estado: Riesgo Moderado. Pausa necesaria.")
            st.write("🧘 **Recomendación:** Técnica de respiración 4-7-8.")
        else: 
            st.error("Estado: Alerta alta. Prioriza tu descanso.")
            st.write("🚨 **Acción:** Técnica 5-4-3-2-1 para Grounding.")
        st.info(f"✨ Frase: {random.choice(['Eres vital.', 'Paso a paso.', 'Tu salud es lo primero.'])}")
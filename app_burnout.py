import streamlit as st
import random

st.set_page_config(page_title="Mente Sana", page_icon="🧠", layout="centered")

# CSS para el estilo TikTok y animación
st.markdown("""
    <style>
    @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-15px); } 100% { transform: translateY(0px); } }
    .mascota-animada { animation: float 3s ease-in-out infinite; font-size: 100px; text-align: center; }
    .stButton>button { border-radius: 20px; background-color: #fe2c55; color: white; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# Sonidos puros (Bips/Trinos sin voz)
def emitir_sonido(tipo):
    frecuencias = {"acariciar": 880, "cantar": 660, "manzana": 440, "diagnostico": 523}
    freq = frecuencias.get(tipo, 440)
    js_code = f"""
    <script>
        var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        var osc = audioCtx.createOscillator();
        osc.type = 'sine';
        osc.frequency.setValueAtTime({freq}, audioCtx.currentTime);
        osc.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.2);
    </script>
    """
    st.components.v1.html(js_code, height=0)

# Datos persistentes
if "registrado" not in st.session_state: st.session_state.registrado = False
if "racha_dias" not in st.session_state: st.session_state.racha_dias = 1

# Banco de preguntas por carrera (Rotación por día)
def obtener_preguntas(carrera, racha):
    bancos = {
        "Medicina": ["¿Lograste descansar?", "¿El estrés clínico pesa?", "¿Comiste bien?", "¿Te sientes actualizado?", "¿La jerarquía te afecta?", "¿Dormiste guardias?", "¿Tu salud mental es prioridad?", "¿Tienes tiempo social?", "¿El ritmo es muy rápido?", "¿Te frustra el estudio?"],
        "Enfermería": ["¿Sientes dolor de espalda?", "¿La carga emocional es alta?", "¿El papeleo te abruma?", "¿Tienes energía física?", "¿El ambiente es caótico?", "¿Te sientes valorado?", "¿Has comido hoy?", "¿Tu sueño es reparador?", "¿El hospital te drena?", "¿Te sientes satisfecho?"],
        "Nutrición": ["¿Cálculos difíciles hoy?", "¿Pacientes que no siguen planes?", "¿Te sientes actualizado?", "¿Mucho estrés metabólico?", "¿Tu dieta está descuidada?", "¿Te frustra el paciente?", "¿Sientes presión docente?", "¿Tienes tiempo personal?", "¿Te sientes seguro?", "¿Mucho estudio hoy?"]
    }
    lista = bancos.get(carrera, bancos["Medicina"])
    random.seed(racha) # La racha determina la semilla para que rote cada día
    return random.sample(lista, 10)

# --- INTERFAZ ---
if not st.session_state.registrado:
    st.markdown("<h1>🧠 Mente Sana</h1>", unsafe_allow_html=True)
    st.session_state.nombre = st.text_input("Nombre:")
    st.session_state.carrera = st.selectbox("Carrera:", ["Medicina", "Enfermería", "Nutrición"])
    if st.button("🚀 Entrar"): st.session_state.registrado = True; st.rerun()
else:
    racha = st.session_state.racha_dias
    avatar = "🐣" if racha < 30 else "🦅🔥"
    st.markdown(f"<div class='mascota-animada'>{avatar}</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    if col1.button("💕 Acariciar"): emitir_sonido("acariciar")
    if col2.button("🎶 Cantar"): emitir_sonido("cantar")

    st.markdown("---")
    preguntas = obtener_preguntas(st.session_state.carrera, racha)
    puntos = 0
    for i, q in enumerate(preguntas):
        res = st.radio(f"{i+1}. {q}", ["Nunca", "A veces", "Seguido", "Siempre"], horizontal=True, key=f"q{i}")
        puntos += {"Nunca": 0, "A veces": 2, "Seguido": 4, "Siempre": 6}[res]

    if st.button("✅ Finalizar Análisis"):
        st.session_state.racha_dias += 1
        emitir_sonido("diagnostico")
        
        st.subheader("📊 Diagnóstico Clínico")
        if puntos <= 15: st.success("¡Excelente estado mental!")
        elif puntos <= 35: 
            st.warning("Nivel Moderado.")
            st.write("🧘 **Recomendación:** Respira 4-4-6 (Inhala, Mantén, Exhala).")
        else:
            st.error("Nivel de Alerta.")
            st.write("🚨 **Acción:** Técnica grounding 5-4-3-2-1.")
        
        st.info(f"✨ Frase: {random.choice(['¡Eres capaz!', 'Paso a paso.', 'Tu salud es lo primero.'])}")
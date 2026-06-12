import streamlit as st
import datetime

# Configuración de la página
st.set_page_config(page_title="MenteSana - Monitor de Burnout", page_icon="🧠", layout="centered")

# --- ESTILOS EN BLOQUE (Notas del Peer) ---
st.title("🧠 MenteSana")
st.subheader("Tu monitor inteligente de estrés y burnout académico")
st.write("Registra tu día para evaluar cómo impacta la carga de estudio en tu cuerpo.")

st.markdown("---")

# --- PANEL LATERAL: HISTORIAL SIMULADO (Para activar el semáforo) ---
st.sidebar.header("📊 Simulador de Historial")
st.sidebar.write("Para probar cómo reacciona el semáforo de la app, simula cómo te has sentido los últimos días:")

simular_crisis = st.sidebar.checkbox("Simular 4 días seguidos en crisis (Estrés 5, <5h sueño, gastritis)", value=False)

# --- 1. PANTALLA DE REGISTRO DIARIO (El Formulario) ---
st.header("📝 Registro Diario (Check-in Nocturno)")
st.caption(f"Fecha de registro: {datetime.date.today().strftime('%d/%m/%Y')}")

# Pregunta 1: Carga Académica
carga_academica = st.slider(
    "1. Carga Académica: ¿Qué tanta tarea, proyectos o estudio tuviste hoy?",
    min_value=1, max_value=5, value=3,
    help="1: Muy ligera / 5: Saturado, sin tiempo libre"
)

# Pregunta 2: Estrés Psicológico
estres_psico = st.select_slider(
    "2. Nivel de Estrés Psicológico: ¿Cómo te sentiste emocionalmente?",
    options=[1, 2, 3, 4, 5],
    value=3,
    format_func=lambda x: {1: "😌 Muy Relajado", 2: "🙂 Tranquilo", 3: "😐 Presionado", 4: "😰 Muy Estresado", 5: "🤯 Al límite / Desbordado"}[x]
)

# Pregunta 3: Manifestaciones Somáticas
st.write("3. Manifestaciones Somáticas: Selecciona los síntomas físicos que presentaste hoy:")
col_sintomas1, col_sintomas2 = st.columns(2)

with col_sintomas1:
    gastritis = st.checkbox("Dolor de estómago / Acidez / Gastritis")
    migrana = st.checkbox("Dolor de cabeza / Migraña")
with col_sintomas2:
    insomnio = st.checkbox("Insomnio / Problemas para dormir")
    tension = st.checkbox("Tensión muscular / Dolor de cuello")

# Pregunta 4: Horas de sueño
horas_sueno = st.number_input("4. Horas de sueño: ¿Cuántas horas dormiste anoche?", min_value=0.0, max_value=24.0, value=7.0, step=0.5)

# --- 2. PANTALLA DE HISTORIAL Y ALERTAS (La Vista de Datos) ---
st.markdown("---")
st.header("🚦 Estado Actual y Semáforo del Burnout")

# Lógica del motor de alertas
# Si el usuario activa el simulador o si el registro de hoy cumple las condiciones críticas
es_crisis_hoy = estres_psico == 5 and horas_sueno < 5.0 and gastritis

if simular_crisis or es_crisis_hoy:
    st.error("🔴 **ALERTA CRÍTICA: SEMÁFORO EN ROJO**")
    st.markdown(
        """
        > 🚨 **¡Ojo! Tu cuerpo está cobrando factura.** Llevas un ritmo insostenible que está afectando tu salud física 
        > (gastritis/insomnio) y mental. Es momento obligatorio de hacer una pausa. No puedes rendir académicamente 
        > si colapsas primero.
        """
    )
elif estres_psico >= 4 or (gastritis or migrana or insomnio or tension):
    st.warning("🟡 **ALERTA PREVENTIVA: SEMÁFORO EN AMARILLO**")
    st.markdown(
        """
        > ⚠️ **Atención:** Tus niveles de estrés están elevados y tu cuerpo está empezando a somatizar (manifestar el estrés físicamente). 
        > Revisa tus horarios de sueño y utiliza las técnicas de la sección de abajo antes de que pases a semáforo rojo.
        """
    )
else:
    st.success("🟢 **SEMÁFORO EN VERDE**")
    st.markdown("> 😎 **¡Vas muy bien!** Tus niveles de estrés son manejables y estás logrando un equilibrio saludable hoy. Sigue así.")

# Métrica visual rápida
st.metric(label="Impacto Físico Detectado", value=f"{sum([gastritis, migrana, insomnio, tension])} de 4 síntomas")

# --- 3. PANTALLA DE PRIMEROS AUXILIOS PSICOLÓGICOS (Recursos) ---
st.markdown("---")
st.header("🩹 Primeros Auxilios Psicológicos")
st.write("Toma un respiro y utiliza estas herramientas avaladas por profesionales de la salud mental:")

tab1, tab2 = st.tabs(["🧘 Respiración Cuadrada", "⏱️ Método Pomodoro"])

with tab1:
    st.subheader("Técnica de Respiración Cuadrada (Reset del Sistema Nervioso)")
    st.write("Esta técnica reduce la ansiedad instantáneamente al activar el sistema nervioso parasimpático:")
    
    # Simulación visual simple de los tiempos
    st.info("Sigue este ritmo mentalmente:")
    st.markdown(
        """
        1. 🫁 **Inhala** profundamente contando hasta **4 segundos**.
        2. 🛑 **Retén** el aire en tus pulmones durante **4 segundos**.
        3. 💨 **Exhala** todo el aire lentamente durante **4 segundos**.
        4. ⏸️ **Espera** con los pulmones vacíos durante **4 segundos** antes de volver a empezar.
        
        *Repite este ciclo 5 veces.*
        """
    )

with tab2:
    st.subheader("Método Pomodoro (Estudio Eficiente sin Agotamiento)")
    st.write("El burnout ocurre por estudiar por horas eternas sin descansos. Aplica esto hoy mismo:")
    
    st.markdown(
        """
        *   **Bloque de Enfoque:** Elige una tarea y trabaja en ella intensamente por **25 minutos** (apaga el celular).
        *   **Descanso Corto:** Detente por **5 minutos** (párate de la silla, estírate, toma agua). No mires redes sociales.
        *   **El Ciclo:** Repite esto 4 veces.
        *   **Descanso Largo:** Después de 4 bloques, regálate un descanso largo de **20 a 30 minutos**.
        """
    )

# Descargo de responsabilidad médico obligatorio
st.markdown("---")
st.caption("⚠️ **Aviso de Salud:** Esta aplicación es una herramienta de monitoreo preventivo y educativo. No sustituye la consulta con un psicólogo, psiquiatra o médico general.")
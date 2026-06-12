import streamlit as st
import random

# Configuración
st.set_page_config(page_title="Mente Sana", page_icon="🧠", layout="centered")

# Inicialización
if "registrado" not in st.session_state: st.session_state.registrado = False
if "racha_dias" not in st.session_state: st.session_state.racha_dias = 1
if "inventario" not in st.session_state:
    st.session_state.inventario = {"🍏 Manzana Dorada": 1, "💡 Lámpara de Incubación": 1, "🌾 Semillas de la Calma": 2}
if "accion_mascota" not in st.session_state: st.session_state.accion_mascota = "¡Hola! Estoy listo para cuidar tu mente."

def obtener_sistema_mascota(racha):
    if racha <= 5: return "🥚", f"Faltan {5 - racha} días para que el huevo rompa."
    elif racha <= 30: return "🐥", "¡Pollito Bebé! Creciendo día a día."
    elif racha <= 60: return "🦆", "¡Pato Silvestre! Disfrutando el camino."
    elif racha <= 90: return "🦉", "¡Búho de Atenea! Sabiduría en tus estudios."
    elif racha <= 120: return "🦅", "¡Águila Real! Volando alto."
    elif racha < 365: return "🦚", "¡Pavo Real! Armonía total."
    else: return "🦅🔥", "¡LEGENDARIO: AVE FÉNIX!"

# Contenido dinámico
def obtener_contenido_diario(carrera, racha):
    consejos = ["Practica la técnica pomodoro.", "Toma agua, tu cerebro lo necesita.", "Escribe tus preocupaciones y rómpelas.", "Regálate 5 minutos de silencio.", "Descansar es avanzar."]
    preguntas_banco = {
        "Medicina": ["¿Cómo va tu energía hoy?", "¿El estrés clínico te pesa hoy?"],
        "Enfermería": ["¿Cansancio físico hoy?", "¿La carga emocional está fuerte?"],
        "Nutrición": ["¿Muchos cálculos hoy?", "¿Has comido bien tú?"]
    }
    return preguntas_banco.get(carrera, ["¿Cómo te sientes?", "¿Mucho estrés?"]), consejos[racha % len(consejos)]

# --- INTERFAZ ---
if not st.session_state.registrado:
    st.title("🧠 Mente Sana")
    nombre = st.text_input("Nombre:")
    carrera = st.selectbox("Carrera:", ["Medicina", "Enfermería", "Nutrición"])
    if st.button("Comenzar"):
        st.session_state.nombre_usuario = nombre
        st.session_state.carrera_usuario = carrera
        st.session_state.registrado = True
        st.rerun()
else:
    st.header(f"Hola {st.session_state.nombre_usuario}")
    avatar, estado = obtener_sistema_mascota(st.session_state.racha_dias)
    
    col1, col2 = st.columns([1, 2])
    col1.markdown(f"<h1 style='font-size:80px'>{avatar}</h1>", unsafe_allow_html=True)
    col2.write(f"**Racha:** {st.session_state.racha_dias} días")
    col2.info(estado)
    
    preguntas, consejo = obtener_contenido_diario(st.session_state.carrera_usuario, st.session_state.racha_dias)
    st.warning(f"💡 {consejo}")
    
    puntos = 0
    for i, q in enumerate(preguntas):
        puntos += st.slider(q, 0, 5, 0)
    
    if st.button("Analizar"):
        st.session_state.inventario[random.choice(list(st.session_state.inventario.keys()))] += 1
        st.success("¡Análisis guardado! Revisa tu mochila.")
        st.rerun()

    # Barra lateral
    if st.sidebar.button("Simular día 365"):
        st.session_state.racha_dias = 365
        st.rerun()
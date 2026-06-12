import streamlit as st
import random

# ... (Mantén toda la parte de configuración, inicialización e inventario igual al código anterior) ...

# LÓGICA DE VARIACIÓN DIARIA (Usamos la racha para variar contenido)
def obtener_contenido_diario(carrera, racha):
    # Consejos que cambian según el día (racha)
    consejos = [
        "Hoy practica la técnica pomodoro: 25 min estudio, 5 descanso.",
        "Recuerda hidratarte bien, ¡tu cerebro necesita agua para procesar toda esa info!",
        "Si hoy te sientes abrumado, escribe en una hoja lo que te preocupa y rómpela.",
        "Regálate 5 minutos de silencio absoluto hoy antes de dormir.",
        "A veces, dejar de estudiar un ratito es la mejor forma de aprender más."
    ]
    # Elegimos un consejo basado en el día
    consejo_del_dia = consejos[racha % len(consejos)]
    
    # Banco de preguntas con variaciones temáticas
    bancos = {
        "Medicina": [
            ["¿Lograste descansar algo después de tu última guardia?", "¿Sientes que la teoría está chocando con la realidad clínica hoy?"],
            ["¿Has tenido tiempo de comer algo nutritivo o solo café?", "¿La presión por aprenderte los cuadros clínicos te está pesando hoy?"]
        ],
        "Enfermería": [
            ["¿Cómo se siente tu espalda después de la jornada de hoy?", "¿La carga emocional de tus pacientes está pesando hoy?"],
            ["¿Lograste terminar todo tu papeleo a tiempo?", "¿Sientes que el ambiente en el hospital fue muy caótico hoy?"]
        ],
        "Nutrición": [
            ["¿Cuántos cálculos dietéticos has tenido que ajustar hoy?", "¿Sientes que tus pacientes siguen tus planes al pie de la letra?"],
            ["¿El estrés te está haciendo descuidar tu propia dieta?", "¿Te sientes actualizado con las últimas tendencias metabólicas?"]
        ]
    }
    
    # Elige preguntas según la carrera y el día
    bloque = bancos.get(carrera, [["¿Cómo va tu energía?", "¿Sientes estrés escolar?"]])
    preguntas_del_dia = bloque[racha % len(bloque)]
    
    return preguntas_del_dia, consejo_del_dia

# ... (Dentro de la lógica de la pantalla, reemplaza el bloque de preguntas fijas por este):

    # Llamamos a nuestra nueva función dinámica
    preguntas_dinamicas, consejo = obtener_contenido_diario(st.session_state.carrera_usuario, st.session_state.racha_dias)
    
    st.info(f"💡 **Consejo para ti hoy:** {consejo}")

    puntos_totales = 0
    # Construir el cuestionario con las preguntas del día
    for i, q in enumerate(preguntas_dinamicas):
        with st.container(border=True):
            seleccion = st.radio(q, list(opciones.keys()), index=0, key=f"p_{i}")
            puntos_totales += opciones[seleccion]
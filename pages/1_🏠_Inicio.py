import streamlit as st

st.title("Contexto")
st.image("movilidad.png", caption="Movilidad urbana")
st.markdown("""
### Descripción
Análisis de costos y tiempos promedio de transporte por departamento.
- **Fuente de datos**: https://github.com/Kalbam/Datos_DATAVIZ/blob/main/movilidad_urbana.csv
- **Variables**: Departamento, Transporte, Tiempo_Promedio_Min, Costo_Promedio_Dia etc.
""")
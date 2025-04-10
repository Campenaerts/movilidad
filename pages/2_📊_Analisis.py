import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv("data/datos.csv")

st.title("Análisis Descriptivo")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Tiempo Promedio", f"{df['Tiempo_Promedio_Min'].mean():.1f} min")
with col2:
    st.metric("Costo Promedio", f"${df['Costo_Promedio_Dia'].mean():.1f} al día")
with col3:
    st.metric("Transportes Únicos", df['Transporte'].nunique())

# Filtro dinámico
transporte = st.selectbox("Selecciona un transporte", df["Transporte"].unique())

# Gráfico de barras (Plotly)
fig = px.bar(
    df[df["Transporte"] == transporte],
    x="Departamento",
    y="Tiempo_Promedio_Min",
    title=f"Tiempo promedio por departamento ({transporte})"
)
st.plotly_chart(fig)

# Tabla resumen
st.dataframe(df.groupby("Departamento").agg({"Costo_Promedio_Dia": "mean"}))
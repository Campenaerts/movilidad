import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap

df = pd.read_csv("data/datos.csv")

st.title("Mapa Interactivo")

# Filtro por tiempo
min_time = int(df["Tiempo_Promedio_Min"].min())
max_time = int(df["Tiempo_Promedio_Min"].max())
tiempo = st.slider("Filtrar por tiempo (min)", min_time, max_time, (min_time, max_time))

# Crear mapa
m = folium.Map(location=[df["Latitud"].mean(), df["Longitud"].mean()], zoom_start=5)

# Añadir marcadores
for _, row in df.iterrows():
    if tiempo[0] <= row["Tiempo_Promedio_Min"] <= tiempo[1]:
        folium.Marker(
            location=[row["Latitud"], row["Longitud"]],
            popup=f"{row['Departamento']} - {row['Tiempo_Promedio_Min']} min",
        ).add_to(m)

# Mostrar mapa
st_folium(m, width=800, height=500)

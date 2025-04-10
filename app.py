import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Movilidad urbana", layout="wide")

with st.sidebar:
    selected = option_menu("Menú", ["Inicio", "Análisis", "Mapas"],
        icons=["house", "bar-chart", "map"], default_index=0)

if selected == "Inicio":
    st.switch_page("pages/1_🏠_Inicio.py")
elif selected == "Análisis":
    st.switch_page("pages/2_📊_Analisis.py")
elif selected == "Mapas":
    st.switch_page("pages/3_🌍_Mapas.py")
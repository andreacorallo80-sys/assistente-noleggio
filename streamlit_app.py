import streamlit as st
from database import DATA

st.set_page_config(page_title="SOS Noleggio", page_icon="🚗")
st.title("🚗 Assistente Contratti NLT")

societa = st.selectbox("Seleziona la Società:", list(DATA.keys()))
argomento = st.radio("Argomento:", list(DATA[societa].keys()))

if societa and argomento:
    st.success(f"📌 {societa} - {argomento}")
    st.info(DATA[societa][argomento])

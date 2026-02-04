import streamlit as st
from database import DATA
st.set_page_config(page_title="Enciclopedia NLT Pro", layout="wide")
st.title("📚 Enciclopedia Operativa NLT")
st.markdown("Consultazione rapida per Customer Care Professionale")
# Selezione società e argomenti
st.sidebar.image("https://img.icons8.com/fluency/96/car.png")
societa = st.sidebar.selectbox("🎯 SELEZIONA SOCIETÀ", list(DATA.keys()))
argomenti = list(DATA[societa].keys())
argomento = st.sidebar.radio("📑 ARGOMENTO", argomenti)
# Recupero dati
res = DATA[societa][argomento]
st.header(f"{societa} - {argomento}")
st.divider()
# Layout a due colonne
col1, col2 = st.columns([1, 1])
with col1:
st.error(f"🔍 **RIFERIMENTO CONTRATTUALE:**\n\n{res['articolo']}")
st.write("")
st.markdown(f"### 💬 COSA DIRE AL CLIENTE:\n{res['spiegazione']}")
with col2:
st.info(f"⚡ **AZIONE IMMEDIATA COLLEGA:**\n\n{res['azione']}")
st.divider()
st.caption("Documentazione interna aggiornata. Estratto dalle Condizioni Generali di Locazione ufficiali.")

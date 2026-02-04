import streamlit as st
from database import DATA

st.set_page_config(page_title="SOS Noleggio - Database Integrale", layout="wide")

st.title("🛡️ Assistente Legale Contratti NLT")
st.markdown("Consultazione ufficiale clausole contrattuali per Customer Care")

# Sidebar di navigazione
with st.sidebar:
    st.header("Seleziona Contratto")
    societa = st.selectbox("Società di Noleggio:", list(DATA.keys()))
    st.divider()
    argomento = st.radio("Seleziona Clausola:", list(DATA[societa].keys()))

# Area Risultati
res = DATA[societa][argomento]

st.subheader(f"Analisi: {argomento}")
st.divider()

# Layout a due blocchi
col1, col2 = st.columns([1, 1])

with col1:
    st.error(f"📄 **RIFERIMENTO ARTICOLO:**\n\n{res['articolo']}")
    st.info(f"📝 **SPIEGAZIONE LEGALE:**\n\n{res['spiegazione']}")

with col2:
    st.success(f"💡 **ISTRUZIONI PER LA COLLEGA (AZIONE):**\n\n{res['azione']}")

st.divider()
st.caption(f"Note: I dati per {societa} sono estratti dalle Condizioni Generali di Locazione aggiornate 2026.")

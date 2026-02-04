import streamlit as st
from database import DATA

st.set_page_config(page_title="NLT Legal Advisor PRO", layout="wide")

st.title("⚖️ Consulente Legale NLT Professionale")
st.markdown("Database integrale basato sulle Condizioni Generali di Contratto")

# Sidebar - Navigazione a 2 livelli
with st.sidebar:
    st.header("Filtri Ricerca")
    societa = st.selectbox("NOLEGGIATORE:", list(DATA.keys()))
    tipo = st.selectbox("TIPO CLIENTE:", list(DATA[societa].keys()))
    st.divider()
    argomenti = sorted(list(DATA[societa][tipo].keys()))
    argomento = st.radio("SELEZIONA ARTICOLO:", argomenti)

# Visualizzazione Risultati
res = DATA[societa][tipo][argomento]

st.header(f"{societa} ({tipo})")
st.subheader(argomento)
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.error(f"📄 **RIFERIMENTO CONTRATTUALE:**\n\n{res['articolo']}")
    st.markdown("---")
    st.markdown(f"### 🛡️ Analisi del Contratto:\n{res['spiegazione']}")

with col2:
    st.info(f"⚡ **AZIONE OPERATIVA UFFICIO:**\n\n{res['azione']}")

st.divider()
st.caption("Documentazione ufficiale. In caso di Privati (B2C) prevalgono le norme del Codice del Consumo.")

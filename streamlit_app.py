import streamlit as st
from database import DATA

st.set_page_config(page_title="AI NLT Advisor PRO", layout="centered")

st.title("🤖 AI Assistente Contratti NLT")
st.markdown("Chiedi aiuto per gestire i clienti e le clausole delle società di noleggio.")

# Selezione Contesto
col1, col2 = st.columns(2)
with col1:
    soc = st.selectbox("Società del contratto:", sorted(list(DATA.keys())))
with col2:
    tipo = st.selectbox("Tipo cliente:", sorted(list(DATA[soc].keys())))

# Input discorsivo (Ragionamento AI)
domanda = st.text_input("Cosa ti chiede il cliente? (es: 'Può andare in Svizzera?' o 'Chi paga i danni?')")

if domanda:
    q = domanda.lower()
    st.divider()
    
    # Motore di interpretazione concettuale
    mappa = {
        "estero": "estero", "viagg": "estero", "paesi": "estero", "svizzera": "estero",
        "incidente": "sinistri", "sinistro": "sinistri", "cai": "sinistri", "danni": "sinistri",
        "prezz": "prezzi", "canone": "prezzi", "ritard": "prezzi",
        "tagliand": "manutenzione", "officina": "manutenzione", "olio": "manutenzione",
        "recedere": "recesso", "chiudere": "recesso", "penale": "recesso",
        "avvocato": "foro", "tribunale": "foro", "causa": "foro", "legal": "foro",
        "sostitutiva": "sostitutiva", "cortesia": "sostitutiva",
        "restituire": "restituzione", "consegnare": "restituzione", "chiavi": "restituzione"
    }

    categoria = None
    for parola, cat in mappa.items():
        if parola in q:
            categoria = cat
            break

    # Visualizzazione Risposta Discorsiva
    regole = DATA[soc][tipo]["regole"]
    
    if categoria and categoria in regole:
        info = regole[categoria]
        with st.chat_message("assistant"):
            st.markdown(f"### 🧐 Analisi per la Collega")
            st.write(f"In merito alla tua domanda su **{soc}**, la risposta si trova nell'**Articolo {info['art']}**.")
            
            st.markdown("---")
            st.write(f"**Cosa dice il contratto:** {info['testo']}")
            
            st.markdown("### 🗣️ Cosa rispondere al cliente")
            st.success(info['ragionamento'])
    else:
        st.warning("Capisco la domanda, ma non trovo una clausola specifica. Prova a usare parole come 'sinistro', 'estero', 'recesso' o 'foro'.")

st.divider()
st.caption("Aggiornato 2026. Basato su CGC Arval B2B (Art. 1-25) e Standard Alphabet/Leasys.")

import streamlit as st
from database import DATA

st.set_page_config(page_title="AI NLT Master Advisor", layout="centered")

st.title("🤖 Assistente NLT Intelligente")
st.markdown("Chiedi aiuto per gestire le richieste dei clienti e le clausole contrattuali.")

# Scelta della società e contesto
col1, col2 = st.columns(2)
with col1:
    soc = st.selectbox("Società del contratto:", sorted(list(DATA.keys())))
with col2:
    tipo_cliente = st.radio("Tipo cliente:", ["Azienda (B2B)", "Privato (B2C)"], horizontal=True)

# Input discorsivo della collega
domanda = st.text_input("Cosa ti chiede il cliente? (es: 'Può andare all'estero?' o 'Chi paga i danni?')")

if domanda:
    q = domanda.lower()
    st.divider()
    
    # Motore di ragionamento (Keyword Matching evoluto)
    mappa = {
        "estero": "estero", "svizzera": "estero", "francia": "estero", "viagg": "estero", "paesi": "estero",
        "incidente": "sinistri", "sinistro": "sinistri", "cai": "sinistri", "danno": "sinistri", "colpa": "sinistri",
        "chiudere": "recesso", "recedere": "recesso", "penale": "recesso", "disdetta": "recesso",
        "officina": "manutenzione", "tagliando": "manutenzione", "olio": "manutenzione", "rottura": "manutenzione",
        "avvocato": "foro", "tribunale": "foro", "causa": "foro", "legale": "foro",
        "sostitutiva": "sostitutiva", "cortesia": "sostitutiva", "macchina": "sostitutiva",
        "restituire": "restituzione", "fine": "restituzione", "chiavi": "restituzione", "pulizia": "restituzione"
    }

    categoria = None
    for parola, cat in mappa.items():
        if parola in q:
            categoria = cat
            break

    # Sezione Risposta Discorsiva
    if categoria and categoria in DATA[soc]["regole"]:
        info = DATA[soc]["regole"][categoria]
        
        st.subheader("🧐 Ragionamento dell'Assistente")
        st.write(f"In base al contratto **{soc}**, questa situazione è regolata dall'**Articolo {info['art']}**.")
        
        st.info(f"**Cosa dice il testo tecnico:** {info['testo']}")
        
        # Logica speciale per il Foro B2C
        if categoria == "foro" and tipo_cliente == "Privato (B2C)":
            st.warning("⚠️ **Attenzione:** Trattandosi di un PRIVATO, non vale il foro della società. Per legge (Codice del Consumo) il foro competente è quello di residenza del cliente.")
        
        st.markdown("### 🗣️ Cosa suggerire al cliente:")
        st.success(info['consiglio'])
    
    elif "totale" in q or "distrutta" in q:
        if "sinistro_totale" in DATA[soc]["regole"]:
            info = DATA[soc]["regole"]["sinistro_totale"]
            st.success(f"Dì al cliente: {info['consiglio']}")
        else:
            st.write("Per questa società, i danni totali seguono la procedura sinistri standard (Art. 7 Arval).")
            
    else:
        st.warning("Non trovo una clausola specifica. Prova a usare parole come: 'sinistro', 'estero', 'foro', 'recesso' o 'manutenzione'.")

st.divider()
st.caption("Aggiornato Febbraio 2026. Basato su CGC Arval B2B (Art. 1-25) e Standard di mercato Alphabet/Leasys/Ayvens/Santander.")

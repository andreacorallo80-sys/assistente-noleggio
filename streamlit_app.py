 import streamlit as st
from database import DATA

st.set_page_config(page_title="AI Legal Advisor NLT", layout="wide")

st.title("🤖 Assistente NLT: Ragionamento Contrattuale")
st.markdown("---")

# Selezione Contesto
col1, col2 = st.columns(2)
with col1:
    soc = st.selectbox("Seleziona la Società", list(DATA.keys()))
with col2:
    tipo = st.radio("Tipo di Cliente", ["Azienda (B2B)", "Privato (B2C)"], horizontal=True)

# Input Discorsivo
domanda = st.text_input("Cosa ti sta chiedendo il cliente? (es: 'Posso andare in Svizzera?' o 'Ho perso le chiavi')")

if domanda:
    d = domanda.lower()
    st.write("### 🔎 Analisi dell'Assistente Virtuale")
    
    # Logica di ragionamento discorsivo
    # Qui simuliamo il ragionamento dell'AI che cerca nel database
    
    context = DATA[soc]["art_chiave"]
    risposta = ""
    consiglio = ""
    articolo = ""

    # Mappatura concettuale
    if "estero" in d or "svizzera" in d or "francia" in d or "viagg" in d:
        info = context.get("estero")
        if info:
            articolo = info['art']
            risposta = f"Per quanto riguarda i viaggi all'estero, **{soc}** specifica che {info['regola']} {info['logica']}"
            consiglio = "Controlla la Carta Verde: se il paese non è barrato, può andare. Se è sbarrato, deve fermarsi e chiederci l'autorizzazione o non avrà copertura assicurativa."

    elif "incidente" in d or "sinistro" in d or "cai" in d or "danno" in d:
        info = context.get("sinistri")
        if info:
            articolo = info['art']
            risposta = f"In caso di incidente, la regola di **{soc}** è chiara: {info['regola']} {info['logica']}"
            consiglio = f"Dì al cliente di inviare il CAI entro i termini ({'24h' if soc=='ALPHABET' else '48h'}). Se non c'è la firma della controparte, avvisalo che Arval/Alphabet gli addebiterà la franchigia piena come colpa sua."

    elif "avvocato" in d or "foro" in d or "tribunale" in d or "causa" in d:
        if tipo == "Azienda (B2B)":
            foro = DATA[soc]["foro_b2b"]
            articolo = "Articolo finale (Foro)"
            risposta = f"Trattandosi di un contratto B2B con **{soc}**, il foro competente è esclusivamente quello di **{foro}**."
            consiglio = f"Se l'avvocato del cliente scrive da un'altra città, fagli presente che la competenza è di {foro}. Spesso questo basta a farli desistere perché i costi di trasferta non convengono."
        else:
            risposta = "Essendo un privato (B2C), prevale il Foro del Consumatore (residenza del cliente)."
            consiglio = "Con i privati non possiamo imporre la sede della società. Dobbiamo essere più concilianti."

    if risposta:
        with st.chat_message("assistant"):
            st.write(f"**Basandomi sull'Articolo {articolo} di {soc}:**")
            st.write(risposta)
            st.info(f"👉 **Suggerimento pratico per te:** {consiglio}")
    else:
        st.warning("Non ho trovato una clausola specifica. Prova a scrivermi parole chiave come 'estero', 'sinistro', 'chiavi' o 'foro'.")

st.divider()
st.caption("Sistema di supporto decisionale interno basato sui PDF Arval, Alphabet e Leasys 2026.")

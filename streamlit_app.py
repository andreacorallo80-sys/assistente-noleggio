import streamlit as st
from database import DATA

st.set_page_config(page_title="AI Assistant Noleggio", layout="centered")

st.title("🤖 Assistente NLT Intelligente")
st.markdown("Chiedi qualunque cosa sui contratti Arval, Alphabet, Leasys...")

# Selezione della società per contestualizzare il ragionamento
societa = st.selectbox("Su quale società stiamo lavorando?", list(DATA.keys()))

# Input discorsivo
domanda = st.text_input("Scrivi qui la tua domanda (es: 'Il cliente può andare all'estero?' o 'Chi paga i danni?')")

if domanda:
    st.divider()
    with st.spinner("Sto analizzando la documentazione..."):
        # Logica di ragionamento AI (Keyword Matching evoluto)
        testo_domanda = domanda.lower()
        trovato = False
        
        regole = DATA[societa]["regole"]
        
        # Mappatura concettuale delle domande
        mappa_concetti = {
            "estero": "conduzione", "guidare": "conduzione", "chi guida": "conduzione",
            "incidente": "sinistri", "botto": "sinistri", "danno": "sinistri", "cai": "sinistri",
            "chiudere": "recesso", "recedere": "recesso", "penale": "recesso",
            "officina": "riparazioni", "meccanico": "riparazioni", "olio": "riparazioni",
            "avvocato": "foro", "tribunale": "foro", "causa": "foro",
            "auto di cortesia": "auto_sostitutiva", "macchina sostitutiva": "auto_sostitutiva",
            "restituire": "restituzione", "consegnare": "restituzione", "fine": "restituzione"
        }

        for chiave, categoria in mappa_concetti.items():
            if chiave in testo_domanda:
                res = regole.get(categoria)
                if res:
                    st.subheader("📌 Ragionamento dell'Assistente")
                    
                    # Risposta discorsiva
                    st.write(f"In base al contratto **{societa}**, la risposta è contenuta nell'**Articolo {res['art']}**.")
                    
                    st.info(f"**Cosa dice il contratto:** {res['testo']}")
                    
                    st.markdown("### 💬 Suggerimento per il cliente:")
                    if categoria == "conduzione":
                        st.success(f"Dì al cliente che può guidare nei paesi UE, ma deve sempre controllare la Carta Verde. Se esce dall'UE, serve l'autorizzazione di {societa} o rischia la rivalsa totale.")
                    elif categoria == "sinistri":
                        st.success(f"Attenzione! Ricorda al cliente che ha solo 48 ore (Arval) o 24 ore (Alphabet). Se non ci manda il CAI firmato, gli addebiteremo l'intero costo del danno anche se ha la Kasko.")
                    elif categoria == "foro":
                        st.success(f"Se il cliente minaccia azioni legali, fagli presente che per contratto il Foro competente è esclusivamente quello di Firenze (Arval) o Roma (Alphabet).")
                    else:
                        st.success("Spiega al cliente che queste sono le condizioni generali firmate in fase di contratto e non sono derogabili.")
                    
                    trovato = True
                    break
        
        if not trovato:
            st.warning("Non ho trovato un articolo specifico per questa domanda. Prova a usare parole come 'sinistro', 'estero', 'recesso' o 'manutenzione'.")

st.divider()
st.caption("AI aggiornata con i PDF Arval B2B (Art. 1-25) e regole generali Alphabet/Leasys.")

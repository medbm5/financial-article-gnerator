import streamlit as st
from dotenv import load_dotenv

# Charger les variables d'environnement à partir d'un fichier .env
load_dotenv()





# Configuration de l'application Streamlit pour un style amélioré
st.title("🧠 Partenaire Conversationnel AI")


st.markdown("""
Bienvenue dans cette application simplifiée de génération de texte AI ! Cette interface conviviale vous permet de générer du texte à partir de vos propres instructions. Idéal pour tout utilisateur, aucune connaissance informatique préalable n'est requise.
""")


# Zone de texte pour l'entrée de l'utilisateur
instruction = st.text_area("Veuillez renseigner vos instructions ici", height=100, key="prompt")

# Configuration de la mise en page en utilisant des colonnes pour l'alignement
col1, col2 = st.columns([0.8, 0.2])

with col1:
    # Bouton Générer pour déclencher la génération de réponse
    if st.button("Générer", key="generate"):
        with st.spinner('🤖 L\'AI réfléchit...'):  # Affiche un spinner pendant le traitement
            response = generate_response(instruction)
            st.text_area("Réponse :", value=response, height=500, key="response", help="Réponse de l'AI")

with col2:
    st.write("")  # Utilisé pour des fins d'alignement
    if st.button("Effacer", key="clear"):
        # Effacer le texte d'instruction ; correction par rapport à la version précédente
        st.session_state.prompt = ""

# Barre latérale pour des informations supplémentaires sur l'application et les détails de configuration
with st.sidebar:
    st.markdown("## Configuration de l'App")
    st.markdown("""
- **Modèle Utilisé :** GPT-3.5 Turbo
- **Température :** 1
- **Max Tokens :** 256
- **Top P :** 1
- **Pénalité de Fréquence :** 0
- **Pénalité de Présence :** 0
    """)

    st.markdown("## À propos")
    st.write("Cette application est alimentée par le GPT-3.5 Turbo d'OpenAI, conçue pour répondre à vos questions, engager une conversation significative et plus encore.")


# Adding the GitHub link as credits
st.markdown('Créé par : [El Mehdi Jebbour](https://github.com/ElMehdijebbour)', unsafe_allow_html=True)
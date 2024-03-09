import streamlit as st
from utils.utils import *
from prompts import economic_note_prompte
import pyperclip
from dotenv import load_dotenv
import pandas as pd

load_dotenv()


def main():
    if 'economic_article' not in st.session_state:
        st.session_state.economic_article = None

    st.title("Generateur d'article economique")


    # les données d'entrées:
    st.header("2. Donner les informations suivantes")

    # Année
    year = st.selectbox('Année', [2023, 2024, 2025], index=0)

    # Trimestre
    trimester = st.selectbox('Trimestre', ['T1', 'T2', 'T3', 'T4'], index=0)


    # Inflation anticipée
    inflation_1_year = st.slider('Inflation anticipée à 1 an (%)', 0.0, 10.0, 5.0)
    inflation_3_5_years = st.slider('Inflation anticipée à 3-5 ans (%)', 0.0, 10.0, 3.0)

    # Date de l'enquête
    survey_date = st.date_input('Date de début de l\'enquête', value=pd.to_datetime('2023-02-20'))
    survey_end_date = st.date_input('Date de fin de l\'enquête', value=pd.to_datetime('2023-03-02'))

    # Méthodologie
    methodology = st.text_area('Méthodologie', 'Enquête auprès de 1000 chefs d\'entreprise')

    # Inflation perçue et officielle
    perceived_inflation = st.number_input('Inflation perçue (%)', value=6.0)
    official_inflation = st.number_input('Inflation officielle (%)', value=6.3)

    # Croissance des salaires anticipée
    anticipated_wage_growth = st.number_input('Croissance des salaires anticipée à un an (%)', value=3.5)

    # Augmentation par rapport au trimestre précédent
    quarterly_increase = st.text_input('Augmentation par rapport au trimestre précédent', '+0.5 points de pourcentage (pp)')

    # Comparaison avec les données historiques
    historical_comparison = st.text_area('Comparaison avec les données historiques', 'inférieure aux taux entre mi-2022 et mi-2023')

    # Distribution des réponses
    response_distribution = st.slider('Distribution des réponses (54% entre 3% et 4%)', 0, 100, 54)

    # Variation trimestrielle
    quarterly_variation = st.text_area('Variation trimestrielle', '+9 pp dans la catégorie 3% à 4%, -10 pp dans la catégorie supérieure à 4%')


    # Format the dates for the information string
    formatted_start_date = survey_date.strftime('%d %B')
    formatted_end_date = survey_end_date.strftime('%d %B')

    # Creating the information string
    article_informations = f"""
    - Année/Trimestre: {year} {trimester}
    - Inflation anticipée à 1 an: {inflation_1_year}%
    - Inflation anticipée à 3-5 ans: {inflation_3_5_years}%
    - Date de l'enquête: {formatted_start_date} au {formatted_end_date}
    - Méthodologie: {methodology}
    - Inflation perçue: {perceived_inflation}%
    - Inflation officielle: {official_inflation}%
    - Croissance des salaires anticipée à un an: {anticipated_wage_growth}%
    - Augmentation par rapport au trimestre précédent: {quarterly_increase}
    - Comparaison avec les données historiques: {historical_comparison}
    - Distribution des réponses: {response_distribution}% des réponses entre 3% et 4%
    - Variation trimestrielle: {quarterly_variation}
    """

    # Generate Cover Letter
    st.header("2. Genérer l'article économique")
    if st.button("Generer l'article"):
        if article_informations is not None :
            prompt_template = economic_note_prompte.prompt_template_classic
            economic_article = generate_economic_article(informations=article_informations, prompt_template=prompt_template)
            st.subheader("Article Economic:")
            st.markdown(economic_article)
            st.session_state.economic_article = economic_article
        else:
            st.warning("Please upload a resume and provide a job listing.")

    # Output Cover Letter
    if st.session_state.economic_article is not None:
        if st.button("Copy to Clipboard"):
            pyperclip.copy(st.session_state.economic_article)
            st.success("Cover letter copied to clipboard!")


if __name__ == "__main__":
    main()

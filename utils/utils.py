from langchain.document_loaders import AsyncChromiumLoader
from agents.gpt_35_turbo import get_agent
from prompts import economic_note_prompte



def generate_economic_article(informations, prompt_template):
    agent = get_agent()
    resp = agent.invoke(prompt_template.format(informations=informations))
    text = resp.content
    return text
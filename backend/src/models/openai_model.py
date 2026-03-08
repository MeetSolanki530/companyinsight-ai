from src.config.settings import get_api_key,get_model_name,get_base_url
from langchain_openai import ChatOpenAI
from src.tools.website_scraper import fetch_webpage
from src.models.response_model import ResponseSchema


def get_model_binded_tool():

    """Get OpenAI LLM With Binded Tools"""

    llm = ChatOpenAI(api_key=get_api_key(),
                     model=get_model_name(),
                     base_url=get_base_url()).bind_tools([fetch_webpage])

    return llm

def get_model_strutured_output():

    """Get OpenAI LLM With Structured Output"""
    
    llm = ChatOpenAI(api_key=get_api_key(),
                     model=get_model_name(),
                     base_url=get_base_url()).with_structured_output(ResponseSchema)

    return llm



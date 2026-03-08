from src.models.openai_model import get_model_binded_tool
from src.config.prompts import WEBSITE_CONTENT_FETCH_AGENT_SYSTEM_PROMPT
from langchain_core.messages import HumanMessage,SystemMessage


def get_website_analysis_agent_response(url : str):
    
    llm = get_model_binded_tool()

    response = llm.invoke(input=[
        SystemMessage(content= WEBSITE_CONTENT_FETCH_AGENT_SYSTEM_PROMPT),
        HumanMessage(content=f"Here is the URL of Website '{url}'.")
    ])

    return response


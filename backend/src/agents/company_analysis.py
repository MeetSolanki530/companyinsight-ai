from src.models.openai_model import get_model_strutured_output
from src.config.prompts import COMPANY_ANALYSIS_AGENT_SYSTEM_PROMPT
from langchain_core.messages import HumanMessage,SystemMessage


def get_company_analysis_agent_response(content):
    
    llm = get_model_strutured_output()

    response = llm.invoke(input=[
        SystemMessage(content= COMPANY_ANALYSIS_AGENT_SYSTEM_PROMPT),
        HumanMessage(content=f"Here is the Content of Website : {content} .")
    ])

    return response


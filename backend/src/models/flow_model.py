from pydantic import BaseModel
from .response_model import ResponseSchema

class WorkflowState(BaseModel):
    url: str
    website_content: str
    analysis_result: ResponseSchema | None = None
from pydantic import BaseModel


class RequestSchema(BaseModel):
    """Request Schema For APi Request Input"""
    url : str



from pydantic import BaseModel


class ResponseSchema(BaseModel):
    """Response Schema For APi Response"""
    company_name : str
    industry : str
    summary : str
    products_services : str
    target_customers : str
    pain_points : str

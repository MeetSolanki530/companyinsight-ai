from fastapi import APIRouter
from src.models.request_model import RequestSchema
from src.workflow.flow import Graph
from fastapi.exceptions import HTTPException


router = APIRouter()

@router.post("/analyze-company")
def analyze_company(request : RequestSchema):
    
    try:
        graph = Graph()

        result = graph.run(request.url)

        return result
    
    except Exception as e:
        raise HTTPException(status_code=500
                            ,detail=f"An Error Occured {str(e)}")

from fastapi import FastAPI
from src.api.routes import router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="Company Insight AI")

app.mount("/static", StaticFiles(directory="../frontend"), name="static")
@router.get("/frontend")
def get_frontend():
    file_path = os.path.join("..", "frontend", "index.html")
    print(file_path)
    return FileResponse(file_path)


app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app=app,port=8080)
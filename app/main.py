from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes import router

app = FastAPI(title="GitHub Connector")

app.include_router(router)

# redirect root to /docs 
@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")

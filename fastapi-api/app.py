from fastapi import FastAPI
from routers import leads

app = FastAPI()

@app.get("/")
async def healthcheck():
    return {"status": "ok"}

app.include_router(leads.router)

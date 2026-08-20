from fastapi import FastAPI, Request
from .routers import leads

app = FastAPI()

@app.get("/")
async def healthcheck():
    return {"status": "ok"}

app.include_router(leads)

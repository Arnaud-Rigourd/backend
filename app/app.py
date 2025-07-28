from fastapi import FastAPI

from app.api.v1.router import api_router

app = FastAPI()


@app.get("/")
async def read_root():
    """A simple endpoint to confirm the server is running."""
    return {"status": "ok"}


app.include_router(api_router, prefix="/api/v1")

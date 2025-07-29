from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def ping():
    """A simple endpoint to confirm the server is running."""
    return {"status": "ok"}


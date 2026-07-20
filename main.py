from fastapi import FastAPI

app = FastAPI(title="Wodby FastAPI boilerplate")


@app.get("/")
async def index() -> dict[str, str]:
    return {"message": "Hello from Wodby FastAPI"}


@app.get("/healthz", include_in_schema=False)
async def healthz() -> dict[str, str]:
    return {"status": "ok"}

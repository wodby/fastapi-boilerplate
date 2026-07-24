from fastapi import FastAPI

from .models import IndexResponse
from .routers import greetings, status


def create_app() -> FastAPI:
    """Create the starter API and register its routers."""
    app = FastAPI(
        title="FastAPI on Wodby",
        summary="A typed API starter deployed with Wodby",
        version="0.1.0",
    )
    app.include_router(status.router)
    app.include_router(greetings.router)

    @app.get("/", response_model=IndexResponse, tags=["meta"])
    async def index() -> IndexResponse:
        return IndexResponse(
            message="Your FastAPI app is running",
            docs="/docs",
            redoc="/redoc",
            openapi="/openapi.json",
        )

    return app

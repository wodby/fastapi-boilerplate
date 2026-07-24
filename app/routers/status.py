import platform
from importlib.metadata import version

from fastapi import APIRouter

from ..models import HealthResponse, StatusResponse

router = APIRouter()


@router.get("/api/status", response_model=StatusResponse, tags=["meta"])
async def application_status() -> StatusResponse:
    """Return typed runtime information."""
    return StatusResponse(
        status="ok",
        runtime=f"Python {platform.python_version()}",
        framework=f"FastAPI {version('fastapi')}",
    )


@router.get(
    "/healthz",
    response_model=HealthResponse,
    include_in_schema=False,
)
async def healthz() -> HealthResponse:
    """Report that the ASGI application can serve requests."""
    return HealthResponse(status="ok")

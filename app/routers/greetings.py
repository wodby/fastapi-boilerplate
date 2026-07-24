from fastapi import APIRouter, status

from ..models import GreetingRequest, GreetingResponse

router = APIRouter(prefix="/api", tags=["examples"])


@router.post(
    "/greetings",
    response_model=GreetingResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_greeting(request: GreetingRequest) -> GreetingResponse:
    """Return a validated response without pretending to persist data."""
    suffix = "!" if request.enthusiastic else "."
    return GreetingResponse(
        message=f"Hello, {request.name}{suffix}",
        framework="FastAPI",
    )

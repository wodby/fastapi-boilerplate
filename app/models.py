from pydantic import BaseModel, Field, field_validator


class IndexResponse(BaseModel):
    """Links exposed by the API root."""

    message: str
    docs: str
    redoc: str
    openapi: str


class StatusResponse(BaseModel):
    """Runtime metadata returned by the status endpoint."""

    status: str
    runtime: str
    framework: str


class HealthResponse(BaseModel):
    """Minimal liveness response."""

    status: str


class GreetingRequest(BaseModel):
    """Validated input for the stateless greeting example."""

    name: str = Field(min_length=1, max_length=80, examples=["Ada"])
    enthusiastic: bool = False

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("name must not be blank")
        return value


class GreetingResponse(BaseModel):
    """Typed output for the greeting example."""

    message: str
    framework: str

# Minimal FastAPI boilerplate

Minimal application for the [Wodby FastAPI service](https://github.com/wodby/service-fastapi) and [FastAPI stack](https://github.com/wodby/stack-fastapi).

The project uses [uv](https://docs.astral.sh/uv/) and includes a Wodby CI pipeline.

## Local development

```shell
uv sync
uv run pytest
uv run fastapi dev
```

Open http://localhost:8000. A health endpoint is available at `/healthz`.

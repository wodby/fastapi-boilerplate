# FastAPI starter for Wodby

A typed API starter for the [Wodby FastAPI service](https://github.com/wodby/service-fastapi) and [FastAPI stack](https://github.com/wodby/stack-fastapi).

It demonstrates:

- application construction and `APIRouter` composition
- Pydantic request and response models
- validation errors and generated OpenAPI documentation
- JSON, health, not-found, and method-not-allowed responses
- pytest, Ruff, Gunicorn with Uvicorn workers, and Wodby CI

## Local development

```shell
uv sync
uv run pytest
uv run fastapi dev
```

Open <http://localhost:8000>. Useful endpoints are:

- `/` — API metadata and documentation links
- `/docs` — interactive Swagger UI documentation
- `/redoc` — ReDoc documentation
- `/api/status` — a typed response example
- `POST /api/greetings` — typed request validation
- `/healthz` — the deployment health endpoint

Try the request model:

```shell
curl -X POST http://localhost:8000/api/greetings \
  -H 'content-type: application/json' \
  -d '{"name":"Ada","enthusiastic":true}'
```

## Project structure

- `main.py` preserves Wodby's `main:app` production entrypoint.
- `app/application.py` creates and composes the API.
- `app/models.py` defines the public request and response contracts.
- `app/routers/` groups related endpoints.

Uvicorn accepts forwarded headers only from configured trusted peers. When
deploying behind a proxy that needs to control client or scheme information,
set `FORWARDED_ALLOW_IPS` to that proxy's explicit addresses. Avoid `*` unless
the application network is isolated so only trusted proxies can connect.

The example API is intentionally stateless: in-memory records would diverge
between Gunicorn workers. Add a persistent datastore when implementing CRUD.

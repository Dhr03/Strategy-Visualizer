# Strategy Visualizer Backend

FastAPI backend for the Formula 1 race strategy visualizer.

## Tech Stack

- FastAPI (async APIs)
- FastF1 (F1 timing & telemetry data)
- Pandas (data processing)
- Redis (optional, for caching)
- Pydantic (schemas)

## Running with Conda

1. **Create environment**

```bash
conda create -n strategy-backend python=3.11 -y
conda activate strategy-backend
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the API**

From this `python-backend` directory:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## Project Layout

See `app/` for application code:

- `app/main.py` – FastAPI app factory and health check
- `app/api/v1` – Versioned API routers and endpoints
- `app/schemas` – Pydantic models (DTOs)
- `app/services` – Domain logic (strategy, FastF1 session loading)
- `app/core` – Config, logging, security stubs
- `app/db` – Database base/session (for future persistence)
- `app/utils` – Helpers (e.g. tire compound mapping)

## Next Steps

This repository currently contains **boilerplate** with unimplemented services.
See `docs/requirements_specs.md` in the root project for the full roadmap.


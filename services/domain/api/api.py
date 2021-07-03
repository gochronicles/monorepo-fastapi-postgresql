from fastapi import FastAPI

# Generic/core routers
from api.routers import (
    domain_router,
)


from starlette.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.include_router(
    domain_router,
    prefix="/api/v1",
    tags=["Domain"],
    responses={418: {"description": "I'm a Domain API"}},
)


# static_dir = os.environ.get("work_dir", "/app/storage")
# os.makedirs(static_dir, exist_ok=True)

# app.mount(static_dir, StaticFiles(directory=static_dir), name="temp")

origins = [
    "http://localhost:3000",
    "http://0.0.0.0:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def ping():
    """[ping func provides a health check]

    Returns:
        [dict]: [success response for health check]
    """
    return {"response": "ping to datahub successful"}

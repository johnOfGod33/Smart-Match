from contextlib import asynccontextmanager

from fastapi import FastAPI

from .auth import routes as auth_routes
from .database import init_db
from .embeddings import routes as embeddings_routes
from .job_offers import routes as job_offers_routes
from .job_seekers import routes as job_seekers_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(job_seekers_routes.router)
app.include_router(auth_routes.router)
app.include_router(job_offers_routes.router)
app.include_router(embeddings_routes.router)

from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from .database import init_db
from .job_seekers.models import Job_seeker

@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
  return {"message": "Hello World"}
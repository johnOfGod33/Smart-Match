from fastapi import APIRouter, HTTPException, Response

from . import utils
from .models import Job_seeker

router = APIRouter(
    prefix="/job_seekers",
    tags=["Job Seekers"],
    responses={
        401: {"description": "Unauthorized"},
        500: {"description": "Internal Server Error"},
    },
)


@router.post("/register", status_code=201)
async def register(job_seeker: Job_seeker):
    try:
        job_seeker.password = utils.hash_password(job_seeker.password)
        await job_seeker.create()
        return Response(status_code=201, content="Job Seeker Registered")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

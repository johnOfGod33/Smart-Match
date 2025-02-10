from fastapi import APIRouter, HTTPException, Response

from ..utils import get_embeddings_data
from . import utils
from .models import Job_seeker

router = APIRouter(
    prefix="/job_seekers",
    tags=["Job Seekers"],
    responses={
        201: {"description": "Job Seeker Registered"},
        401: {"description": "Unauthorized"},
        500: {"description": "Internal Server Error"},
    },
)


@router.post("/register", status_code=201, response_model=str)
async def register(job_seeker: Job_seeker):
    try:
        job_seeker.password = utils.hash_password(job_seeker.password)

        text = utils.prepare_data_for_embedding(job_seeker)
        job_seeker.seeker_embeddings = get_embeddings_data(text)

        await job_seeker.create()
        return Response(status_code=201, content="Job Seeker Registered")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

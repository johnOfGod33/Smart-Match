from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.responses import JSONResponse

from ..auth.utils import get_current_user
from ..schemas import Message
from ..utils import get_embeddings_data
from . import utils
from .models import Job_seeker

router = APIRouter(
    prefix="/job_seekers",
    tags=["Job Seekers"],
    responses={
        200: {"descripiton": "Job Seeker profile"},
        201: {"description": "Job Seeker Registered"},
        401: {"description": "Unauthorized"},
        404: {"description": "Job Seeker not found"},
        500: {"description": "Internal Server Error"},
    },
)


@router.post("/register", responses={201: {"model": Message}})
async def register(job_seeker: Job_seeker):
    try:
        job_seeker_exists = await Job_seeker.find_one(
            Job_seeker.email == job_seeker.email
        )

        if job_seeker_exists:
            raise HTTPException(status_code=404, detail="Job Seeker already exists")

        job_seeker.password = utils.hash_password(job_seeker.password)
        text = utils.prepare_data_for_embedding(job_seeker)
        job_seeker.seeker_embeddings = get_embeddings_data(text)

        await job_seeker.create()

        return JSONResponse(
            status_code=201, content={"message": "Job Seeker Registered"}
        )
    except HTTPException as err:
        raise err
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"some error occured {err}")


@router.get("/me/", status_code=200, response_model=Job_seeker)
async def get_me(user: Annotated[Job_seeker, Security(get_current_user)]):
    return user

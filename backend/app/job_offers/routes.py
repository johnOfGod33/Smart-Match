from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, Response

from ..auth.utils import get_current_user
from ..job_seekers.models import Job_seeker
from ..utils import get_embeddings_data
from . import utils
from .models import Job_offer

router = APIRouter(
    prefix="/job_offers",
    tags=["Job Offers"],
    responses={
        401: {"description": "Unauthorized"},
        500: {"description": "Internal Server Error"},
    },
)


@router.get("/", status_code=200, response_model=List[Job_offer])
async def get_job_offers(
    job_seeker: Annotated[Job_seeker, Depends(get_current_user)],
):
    try:
        job_offers = await Job_offer.find().to_list()
        return job_offers
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"somme error ocurred {err}")


@router.post("/", status_code=201)
async def create_job_offer(
    job_offers: List[Job_offer],
    job_seeker: Annotated[Job_seeker, Depends(get_current_user)],
):
    try:
        for job_offer in job_offers:
            text = utils.prepare_data_for_embedding(job_offer)
            job_offer.offer_embeddings = get_embeddings_data(text)
            await job_offer.create()

        return Response(status_code=201, content="Job Offer Created")
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"somme error ocurred {err}")

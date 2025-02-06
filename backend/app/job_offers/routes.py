from typing import Annotated, Any, Dict, List

from fastapi import APIRouter, Depends, HTTPException, Response

from ..auth.utils import get_current_user
from ..job_seekers.models import Job_seeker
from ..job_seekers.schemas import Job_seeker_base
from ..utils import get_embeddings_data
from . import utils
from .models import Job_offer
from .schemas import Job_offer_with_score

router = APIRouter(
    prefix="/job_offers",
    tags=["Job Offers"],
    responses={
        200: {"description": "Job Offers"},
        201: {"description": "Job Offer Created"},
        401: {"description": "Unauthorized"},
        500: {"description": "Internal Server Error"},
    },
)


@router.get("/", status_code=200)
async def get_best_job_offers(
    job_seeker: Annotated[Job_seeker, Depends(get_current_user)],
):

    try:
        query = [
            {
                "$vectorSearch": {
                    "index": "vector_index",
                    "queryVector": job_seeker.seeker_embeddings,
                    "path": "offer_embeddings",
                    "numCandidates": 100,
                    "limit": 15,
                },
            },
            {"$match": {"domain": job_seeker.domain}},
            {
                "$project": {
                    "_id": 0,
                    "score": {"$meta": "vectorSearchScore"},
                    "title": 1,
                    "domain": 1,
                    "skills_required": 1,
                    "type_offer": 1,
                    "years_of_experience_required": 1,
                }
            },
        ]

        job_offers = await Job_offer.aggregate(
            query, projection_model=Job_offer_with_score
        ).to_list()

        for job_offer in job_offers:
            job_offer = utils.update_score(job_seeker, job_offer)

        job_offers.sort(key=lambda job_offer: job_offer.score, reverse=True)

        return {"job_seeker": job_seeker, "job_offers": job_offers}
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"somme error ocurred {err}")


@router.post("/", status_code=201)
async def create_job_offer(
    job_offers: List[Job_offer],
    job_seeker: Annotated[Job_seeker_base, Depends(get_current_user)],
):
    try:
        for job_offer in job_offers:
            text = utils.prepare_data_for_embedding(job_offer)
            job_offer.offer_embeddings = get_embeddings_data(text)
            await job_offer.create()

        return Response(status_code=201, content="Job Offer Created")
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"somme error ocurred {err}")


""" @router.update("/embedding/{job_offer_id}", status_code=200)
async def update_embedding(job_offer_id: str, skills: List[str]):
    try:
        job_offer = await Job_offer.get(job_offer_id)
        job_offer.skills_required = skills
        await job_offer.update()

        return Response(status_code=200, content="Job Offer Updated")
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"somme error ocurred {err}")
 """

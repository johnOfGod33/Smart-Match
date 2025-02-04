from typing import List, Annotated

from ..job_seekers.models import Job_seeker
from fastapi import APIRouter, Depends, HTTPException
from .models import Job_offer
from ..auth import utils

router = APIRouter(prefix="/job_offers", tags=["Job Offers"], responses={401: {"description": "Unauthorized"}, 500: {"description": "Internal Server Error"}})

@router.get('/', status_code=200, response_model=List[Job_offer])
async def get_job_offers(job_seeker: Annotated[Job_seeker, Depends(utils.get_current_user)]):
  try:
    job_offers = await Job_offer.find().to_list()
    return job_offers
  except Exception as err:
    raise HTTPException(status_code=500, detail=f'somme error ocurred {err}')
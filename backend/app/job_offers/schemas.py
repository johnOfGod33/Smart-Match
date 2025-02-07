from typing import List

from pydantic import BaseModel

from ..schemas import Job_offer_type


class Job_offer_base(BaseModel):
    title: str
    domain: str
    skills_required: List[str]
    type_offer: Job_offer_type
    years_of_experience_required: int


class Job_offer_with_score(Job_offer_base):
    score: float | None

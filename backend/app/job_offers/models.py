from typing import List

from beanie import Document, Indexed

from ..schemas import Job_offer_type


class Job_offer(Document):
    title: str
    domain: str
    skills_required: List[str]
    type_offer: Job_offer_type
    years_of_experience_required: int
    offer_embeddings: List[float]

from typing import List

from beanie import Document

from .schemas import Job_offer_base


class Job_offer(Job_offer_base, Document):
    """model use for db storage"""

    skills_embeddings: List[float] = []
    years_embeddings: List[float] = []
    type_offer_embeddings: List[float] = []
    offer_embeddings: List[float]

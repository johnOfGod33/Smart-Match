from typing import List

from beanie import Document

from ..schemas import Job_offer_type
from .schemas import Job_offer_base


class Job_offer(Job_offer_base, Document):
    offer_embeddings: List[float]

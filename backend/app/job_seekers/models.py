from typing import List

from beanie import Document

from .schemas import Job_seeker_base


class Job_seeker(Job_seeker_base, Document):
    """model use for db storage"""

    seeker_embeddings: List[float] = []

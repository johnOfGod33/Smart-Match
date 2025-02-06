from typing import List

from beanie import Document
from pydantic import Field

from .schemas import Job_seeker_base


class Job_seeker(Job_seeker_base, Document):
    """model use for db storage"""

    seeker_embeddings: List[float] = []


class Job_seeker_authenticate(Job_seeker_base, Document):
    class Config:
        fileds = {"password": {"exclude": True}}

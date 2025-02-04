from typing import List

from .schemas import Job_seeker_base
from ..schemas import Job_offer_type
from beanie import Document

class Job_seeker(Job_seeker_base, Document):
  domain: str
  skills: List[str]
  type_offer_seeker: Job_offer_type
  years_of_experience: int
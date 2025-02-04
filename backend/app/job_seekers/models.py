from typing import List

from ..schemas import Job_offer_type
from pydantic import EmailStr
from beanie import Document

class Job_seeker(Document):
  first_name: str
  last_name: str
  email: EmailStr
  password: str
  domain: str
  skills: List[str]
  type_offer_seeker: Job_offer_type
  years_of_experience: int
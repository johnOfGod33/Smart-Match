from typing import List

from pydantic import BaseModel, EmailStr, Field, SecretStr

from ..schemas import Job_offer_type


class Job_seeker_in(BaseModel):
    """schema use for login"""

    email: EmailStr
    password: str


class Job_seeker_base(Job_seeker_in):
    """schema use for register"""

    first_name: str
    last_name: str
    domain: str
    skills: List[str]
    type_offer_seeker: Job_offer_type
    years_of_experience: int

from typing import Annotated, List

from beanie import Document, Indexed
from pydantic import ConfigDict, EmailStr

from .schemas import Job_seeker_base


class Job_seeker(Job_seeker_base, Document):
    """model use for db storage"""

    email: Annotated[EmailStr, Indexed(unique=True)]
    seeker_embeddings: List[float] = []

    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "user@example.com",
                "password": "password",
                "first_name": "jean de dieu",
                "last_name": "SESSOU",
                "domain": "Finance",
                "skills": ["python"],
                "type_offer_seeker": "internship",
                "years_of_experience": 3,
            }
        }
    }

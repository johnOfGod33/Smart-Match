from enum import Enum

from pydantic import BaseModel


class Job_offer_type(str, Enum):
    internship = "internship"
    full_time = "full_time"
    part_time = "part_time"
    freelance = "freelance"
    volunteer = "volunteer"


class Message(BaseModel):
    message: str

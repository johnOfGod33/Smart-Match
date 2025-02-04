from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from .job_offers.models import Job_offer
from .job_seekers.models import Job_seeker


async def init_db() -> None:
    client = AsyncIOMotorClient("mongodb://127.0.0.1:27017")

    db = client.smart_match

    await init_beanie(database=db, document_models=[Job_offer, Job_seeker])

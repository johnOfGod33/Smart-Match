from collections.abc import AsyncIterator

import pytest
import pytest_asyncio
from app.job_offers.models import Job_offer
from app.job_seekers.models import Job_seeker
from app.job_seekers.utils import hash_password
from app.main import app
from asgi_lifespan import LifespanManager
from beanie import init_beanie
from httpx import ASGITransport, AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient


def test_print():
    print("test")
    assert True


@pytest_asyncio.fixture
async def setup_database():
    """Setup the fake database"""
    client = AsyncIOMotorClient("mongodb://localhost:27017/")

    db = client.smart_match_test

    print("start initialize database")
    await init_beanie(database=db, document_models=[Job_offer, Job_seeker])
    print("end initialize database")

    yield db

    print("start clean db")
    await db.drop_collection("Job_offer")
    await db.drop_collection("Job_seeker")
    client.close()
    print("end cleaning")


@pytest_asyncio.fixture()
async def client() -> AsyncIterator[AsyncClient]:
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app), base_url="http://test"
        ) as _client:
            try:
                yield _client
            except Exception as err:
                print(err)


@pytest_asyncio.fixture
async def create_job_seeker(setup_database):
    user_data = {
        "email": "mytester@example.com",
        "password": "test1234",
        "first_name": "tester",
        "last_name": "TESTER",
        "domain": "Finance",
        "skills": ["python"],
        "type_offer_seeker": "internship",
        "years_of_experience": 1,
    }

    job_seeker = Job_seeker(**user_data)
    job_seeker.password = hash_password(job_seeker.password)

    await job_seeker.create()
    print("job seeker created", job_seeker)
    yield job_seeker
    print("job seeker deleted")

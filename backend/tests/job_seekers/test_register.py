import pytest
from app.job_seekers.models import Job_seeker
from app.main import app
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_register(client: AsyncClient, setup_database):
    user_data = {
        "email": "user@example.com",
        "password": "password",
        "first_name": "jean de dieu",
        "last_name": "SESSOU",
        "domain": "Finance",
        "skills": ["python"],
        "type_offer_seeker": "internship",
        "years_of_experience": 3,
    }

    response = await client.post(
        "/job_seekers/register", json=dict(Job_seeker(**user_data))
    )

    assert response.status_code == 201
    assert response.json() == "Job Seeker Registered"

    job_seeker = await Job_seeker.find_one(Job_seeker.email == user_data.get("email"))
    assert job_seeker is not None
    assert job_seeker.email == user_data.get("email")


@pytest.mark.asyncio
async def test_create_job_seeker(setup_database):
    user_data = {
        "email": "qkljdfkf@example.com",
        "password": "password",
        "first_name": "jean de dieu",
        "last_name": "SESSOU",
        "domain": "Finance",
        "skills": ["python"],
        "type_offer_seeker": "internship",
        "years_of_experience": 3,
    }
    job_seeker = Job_seeker(**user_data)

    await job_seeker.create()

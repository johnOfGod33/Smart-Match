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

    response = await client.post("/job_seekers/register", json=user_data)

    assert response.status_code == 201
    assert response.json() == {"message": "Job Seeker Registered"}

    job_seeker = await Job_seeker.find_one(Job_seeker.email == user_data.get("email"))

    assert job_seeker is not None
    assert job_seeker.email == user_data.get("email")
    assert job_seeker.password != user_data.get("password")
    assert job_seeker.seeker_embeddings.__len__() == 384


@pytest.mark.asyncio
async def test_resgister_fail_duplicate_email(client: AsyncClient, setup_database):
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

    response = await client.post("/job_seekers/register", json=user_data)
    assert response.status_code == 201

    response = await client.post("/job_seekers/register", json=user_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "Job Seeker already exists"}


@pytest.mark.asyncio
async def test_resgister_fail_bad_body(client: AsyncClient, setup_database):
    user_data = {}
    response = await client.post("/job_seekers/register", json=user_data)
    assert response.status_code == 422

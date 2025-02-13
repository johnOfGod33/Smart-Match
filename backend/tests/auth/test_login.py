""" Test the login route 

Deux reponse possnible :
    avant besoin de créer un user
    - 200 : si le login reussi avec creation du token a verifier
    - 401 : si le login fail avec un message d'erreur
      - mauvais email 
      - bon email mais mauvais mot de passe

    - 500 : si une erreur est survenue
"""

import pytest
from fastapi import HTTPException
from httpx import AsyncClient
from starlette.exceptions import HTTPException


@pytest.mark.asyncio
async def test_login(client: AsyncClient, create_job_seeker):
    user_input = {
        "email": "mytester@example.com",
        "password": "test1234",
    }

    response = await client.post("/auth/login", json=user_input)

    assert response.status_code == 200
    assert response.json().get("access_token") is not None
    assert response.json().get("token_type") == "bearer"


@pytest.mark.asyncio
async def test_login_fail_bad_email(client: AsyncClient, create_job_seeker):
    user_input = {
        "email": "bademailtest@example.com",
        "password": "test1234",
    }

    response = await client.post("/auth/login", json=user_input)

    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}


@pytest.mark.asyncio
async def test_login_fail_bad_password(client: AsyncClient, create_job_seeker):
    user_input = {
        "email": "mytester@example.com",
        "password": "badpassword",
    }

    response = await client.post("/auth/login", json=user_input)

    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}


@pytest.mark.asyncio
async def test_login_fail_bad_body(client: AsyncClient, create_job_seeker):
    user_input = {}
    response = await client.post("/auth/login", json=user_input)

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_login_server_error(client: AsyncClient, create_job_seeker):
    user_input = {
        "email": "mytester@example.com",
        "password": "test1234",
    }

    with pytest.raises(HTTPException) as excinfo:
        await client.post("/auth/login", json=user_input)
        raise HTTPException(status_code=500, detail="somme error ocurred some_error")

    assert excinfo.value.status_code == 500
    assert excinfo.value.detail == "somme error ocurred some_error"

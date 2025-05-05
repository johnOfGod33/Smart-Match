from fastapi import APIRouter, HTTPException, status

from ..job_seekers.schemas import Job_seeker_in
from . import utils
from .schemas import Token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={
        401: {
            "description": "Unauthorized, invalid credentials or access token",
            "headers": {"WWW-Authenticate": "Bearer"},
        },
        500: {"description": "Internal Server Error"},
    },
)


@router.post("/login", status_code=200, response_model=Token)
async def login(job_seeker: Job_seeker_in) -> Token:
    try:
        job_seeker = await utils.authenticate_user(
            job_seeker.email, job_seeker.password
        )

        if not job_seeker:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token = utils.create_access_token(job_seeker.id)

        return Token(access_token=access_token, token_type="bearer")
    except Exception as err:
        raise err
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"somme error ocurred {err}")

from passlib.context import CryptContext

from .models import Job_seeker

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def prepare_data_for_embedding(job_seeker: Job_seeker):
    text_skills = "skills : " + ",".join(job_seeker.skills)
    text_type_offer = "type offer : " + job_seeker.type_offer_seeker.value
    text_years_of_experience = "years of experience : " + str(
        job_seeker.years_of_experience
    )

    text = text_skills + "." + text_type_offer + "." + text_years_of_experience
    return text

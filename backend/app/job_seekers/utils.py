import bcrypt

from .models import Job_seeker


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password, bcrypt.gensalt())


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password, hashed_password)


def prepare_data_for_embedding(job_seeker: Job_seeker):
    text_skills = ",".join(job_seeker.skills)

    text = (
        f"user is looking for a job in {job_seeker.domain}. "
        f"They have experience in the following skills: {text_skills}. "
        f"They are looking for a {job_seeker.type_offer_seeker.value} position"
        f"and have {job_seeker.years_of_experience} years of experience."
    )
    return text

from ..job_seekers.models import Job_seeker
<<<<<<< HEAD
=======
from ..utils import get_similarity_score
>>>>>>> feat/optimize_scoring_with_many_embedding
from .models import Job_offer
from .schemas import Job_offer_with_score


def prepare_data_for_embedding(job_offer: Job_offer):
    text_skills_required = ", ".join(job_offer.skills_required)
    text = (
        f"This job requires the following skills: {text_skills_required}. "
        f"It is a {job_offer.type_offer.value} position requiring {job_offer.years_of_experience_required} years of experience."
    )

    return text


def update_score(job_seeker: Job_seeker, job_offer: Job_offer_with_score):
    domain_score = 1 if job_offer.domain == job_seeker.domain else 0
    skills_score = sum(
        1 for skill in job_offer.skills_required if skill in job_seeker.skills
    ) / len(job_offer.skills_required)

    if job_seeker.years_of_experience > job_offer.years_of_experience_required:
        years_experience_score = 1
    else:
        if job_offer.years_of_experience_required == 0:
            years_experience_score = 0
        else:
            years_experience_score = (
                job_seeker.years_of_experience / job_offer.years_of_experience_required
            )

    job_offer.score = (
        job_offer.score + domain_score + skills_score + years_experience_score
    ) / 4.0

    return job_offer
<<<<<<< HEAD
=======


def update_score_v2(job_seeker: Job_seeker, job_offer: Job_offer_with_score):
    domain_score = 1 if job_offer.domain == job_seeker.domain else 0
    skills_score = skills_score = get_similarity_score(
        f"i'm have skill in {', '.join(job_seeker.skills)}",
        f"you have to have skill in {', '.join(job_offer.skills_required)}",
    )

    print(skills_score)

    year_experience = get_similarity_score(
        f"i have {job_seeker.years_of_experience} years of experience",
        f"you have to have {job_offer.years_of_experience_required} years of experience",
    )

    print(year_experience)

    job_offer.score = (
        job_offer.score + domain_score + skills_score + year_experience
    ) / 4.0

    return job_offer
>>>>>>> feat/optimize_scoring_with_many_embedding

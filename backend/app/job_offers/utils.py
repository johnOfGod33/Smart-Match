from .models import Job_offer


def prepare_data_for_embedding(job_offer: Job_offer):
    text_skills_required = "skills : " + ",".join(job_offer.skills_required)
    text_type_offer = "type offer : " + job_offer.type_offer.value
    text_years_of_experience_required = "years of experience : " + str(
        job_offer.years_of_experience_required
    )

    text = (
        text_skills_required
        + "."
        + text_type_offer
        + "."
        + text_years_of_experience_required
    )
    return text

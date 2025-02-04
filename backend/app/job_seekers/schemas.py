from pydantic import BaseModel, EmailStr

class JobSeekerBase(BaseModel):
  first_name: str
  last_name: str
  email: EmailStr

class JobSeekerIn(JobSeekerBase):
  password: str
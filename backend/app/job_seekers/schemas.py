from pydantic import BaseModel, EmailStr

class Job_seeker_in(BaseModel):
  email: EmailStr
  password: str

class Job_seeker_base(Job_seeker_in):
  first_name: str
  last_name: str
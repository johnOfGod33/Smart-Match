from typing import List
from pydantic import BaseModel,EmailStr
from beanie import Link, Indexed

class Token(BaseModel):
  access_token: str
  token_type: str
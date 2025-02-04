from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer
from datetime import datetime, timezone, timedelta
from ..job_seekers.models import Job_seeker
import jwt
from jwt.exceptions import InvalidTokenError
from beanie import PydanticObjectId
from ..configs import settings
from ..job_seekers.utils import verify_password

oauth2_scheme = HTTPBearer(auto_error=False)

def create_access_token(user_id:str):
    to_encode = {"user_id": str(user_id)}
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.JWT_EXPIRE_IN)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

    return encoded_jwt

async def authenticate_user(email: str, password: str):
    try:
      user = await Job_seeker.find_one(Job_seeker.email == email)
      
      if not user:
          return False
      
      if not verify_password(password, user.password):
          return False
            
      return user
    
    except Exception as err:
        raise HTTPException(status_code=500, detail=f'somme authentication error ocurred {err}')
    
async def get_current_user(token: str = Depends(oauth2_scheme)):
    print(token)
    credentials_exception = HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Could not validate credentials",
      headers={"WWW-Authenticate": "Bearer"},)
    
    try:
        payload = jwt.decode(token.credentials, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        user_id = payload.get("user_id")

        if not user_id:
            raise credentials_exception
        
        user = await Job_seeker.find_one(Job_seeker.id == PydanticObjectId(user_id))
        
        if not user:
            print('error')
            raise credentials_exception
        
        return user
    except InvalidTokenError:
        raise credentials_exception
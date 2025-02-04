from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  SECRET_KEY: str
  JWT_ALGORITHM: str
  JWT_EXPIRE_IN: int
  model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
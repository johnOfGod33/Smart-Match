from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_EXPIRE_IN: int
    MONGO_URI: str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

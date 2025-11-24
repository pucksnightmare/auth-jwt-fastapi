from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Auth JWT FastAPI"
    APP_VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./auth.db"
    JWT_SECRET: str = "supersecret"
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()

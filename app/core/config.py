from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Auth API"
    APP_VERSION: str = "1.0.0"

    DB_NAME: str = "auth.db"

    JWT_SECRET_KEY: str = "supersecretkey"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"

settings = Settings()

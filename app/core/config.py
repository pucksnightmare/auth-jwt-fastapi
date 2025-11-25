from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Auth API"
    APP_VERSION: str = "1.0.0"

    # --- JWT ---
    SECRET_KEY: str = "supersecretkey123"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # --- DB ---
    DATABASE_URL: str = "sqlite:///./app.db"

    class Config:
        env_file = ".env"

settings = Settings()

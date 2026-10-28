from email_validator import validate_email
from email_validator import validate_email
from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    # Database (must use the asyncpg driver)
    DATABASE_URL : str
    # Auth
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRY_IN_MINUTES : int
    REFRESH_TOKEN_EXPIRY_IN_DAYS : int
    JWT_SECRET_KEY : str

    # AI triage agent (Google AI Studio key)
    GOOGLE_API_KEY : str
    MODEL_NAME : str
    GOOGLE_MODEL_PROVIDER : str

    # Service to service communication creds
    SERVICE_ACTIVATION_TOKEN : str

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=True 
    )


settings = Settings()
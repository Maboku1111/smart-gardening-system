from pydantic_settings import BaseSettings

class CommonSettings(BaseSettings):
    """
    Common settings for the application.
    """
    APP_NAME: str = "Smart Gardening System"
    DEBUG_MODE: bool = False

class ServerSettings(BaseSettings):
    """
    Settings for the server.
    """
    HOST: str = "127.0.0.1"
    PORT: int = 8001

class DatabaseSettings(BaseSettings):
    """
    Settings for the database.
    """
    REALM_APP_ID: str
    DB_URL: str
    DB_NAME: str

class AuthSettings(BaseSettings):
    """
    Settings for authentication.
    """
    JWT_SECRET_KEY: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    SECURE_COOKIE: bool = False

class ExternalAPIsSettings(BaseSettings):
    """
    Settings for external APIs.
    """
    STORMGLASS_API_KEY: str
    OPENWEATHERMAP_API_KEY: str
    ADMINKINDWISE_API_KEY: str
    AGROMONITORING_API_KEY: str

class Settings(CommonSettings, ServerSettings, DatabaseSettings, AuthSettings, ExternalAPIsSettings):
    """
    Main settings class that combines all the settings from the other classes.
    """
    class Config:
        env_file = ".env"

settings = Settings()


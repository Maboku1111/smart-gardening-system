from pydantic_settings import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "smart-gardening-system"
    DEBUG_MODE: bool = False

class ServerSettings(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8001

class DatabaseSettings(BaseSettings):
    DB_URL: str
    DB_NAME: str

class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    stormglass_api_key: str
    openweathermap_api_key: str
    adminkindwise_api_key: str
    agromonitoring_api_key: str

    class Config:
        env_file = ".env"


settings = Settings()
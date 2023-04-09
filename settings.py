from pydantic import BaseSettings

class Settings(BaseSettings):
    SERVICE_NAME: str = "Mime Test"
    API_INSTANCE: str = "local/gpu_1"
    VERSION: str = "0.0.1"

    class Config:
        case_sensitive = True


settings = Settings()
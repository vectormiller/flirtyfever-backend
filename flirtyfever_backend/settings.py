from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MAIN_URL: str

settings = Settings()
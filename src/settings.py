from pydantic_settings import BaseSettings
from pydantic import PostgresDsn
from dotenv import load_dotenv, dotenv_values
from os import getenv
from exceptions import EnvVarLoadingException

load_dotenv()

class Settings(BaseSettings):
    DB_URL: PostgresDsn
    ROOT_URL: str

def load_settings() -> Settings:
    """
    Loads settings from environments varibales to Settings
    pydantic model. With dotenv module .env file is parsed into
    environment variables. This function loads .env content
    into Settings structure. 

    Returns:
    Settings - pydantic model with app settings
    """
    creds = {}
    for field_name in Settings.model_fields.keys():
        creds[field_name] = getenv(field_name)

    return Settings(**creds)

try:
    settings = load_settings()
except Exception as e:
    raise EnvVarLoadingException(e)

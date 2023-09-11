"""
    Settings Module

    This module is responsible for managing application settings and environment variables using Pydantic.

    Modules and Packages:
        - os: Provides access to operating system functionalities.
        - pydantic_settings: BaseSettings class for creating Pydantic-based settings models.
        - pydantic: Provides data validation and parsing using Python data types.
        - dotenv: Loads environment variables from a .env file.
        - exceptions: Custom exception for handling environment variable loading errors.

    Classes:
        - Settings: Pydantic model for defining application settings, such as database URL and root URL.

    Functions:
        - load_settings: Loads settings from environment variables into the Settings Pydantic model.

    Usage:
        1. Import the `settings` object to access application settings.
            Ex: from settings import settings
        2. Get needed environment variable.
            Ex: SQLACLHEMY_URL = str(settings.DB_URL)

    Configuration:
        - See .env_example  file to discover which variables should be in the environment.
        - Use a .env file to define environment variables for your application settings.
"""

from os import getenv
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn
from dotenv import load_dotenv, dotenv_values # pylint: disable=unused-import
from exceptions import EnvVarLoadingException

load_dotenv()

class Settings(BaseSettings):
    """
        Project Environment Variables
    """
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
    for field_name in Settings.model_fields:
        creds[field_name] = getenv(field_name)

    return Settings(**creds)

try:
    settings = load_settings()
except Exception as e:
    raise EnvVarLoadingException(e) from e

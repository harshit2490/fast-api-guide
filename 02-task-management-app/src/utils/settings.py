# This file will be used to load environment variables

# BaseSettings -> This is a class that is used to load environment variables
# SettingsConfigDict -> This is used to specify the location of the environment variables
# env_file=".env" -> This will load the environment variables from the .env file
# extra='ignore' -> This will ignore any extra environment variables

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra='ignore')
    DB_CONNECTION_STRING:str
    SECRET_KEY:str
    ALGORITHM:str
    ACCESS_TOKEN_EXPIRE_MINUTES:int

settings = Settings()
    
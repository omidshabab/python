from pydantic import BaseSettings

class Settings(BaseSettings):
    env_name: str 
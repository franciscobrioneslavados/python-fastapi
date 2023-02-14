from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGO_USERNAME: str
    MONGO_PASSWORD: str
    MONGO_DATABASE: str 
    MONGO_URL: str

    class Config:
        env_file = './.env'

settings = Settings()

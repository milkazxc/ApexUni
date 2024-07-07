import os

from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

current_dir = os.path.dirname(__file__)

DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")

class Settings(BaseSettings):
    DB_HOST: str

    DB_PORT: str

    DB_NAME: str

    DB_USER: str

    DB_PASS: str

    class Config:
        env_file = ".env"
    @property
    def db_url_postgresql(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
settings_ = Settings()
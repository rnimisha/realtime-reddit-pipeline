from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    CLIENT_SECRET: str
    USER_AGENT: str
    CLIENT_ID: str

    class Config:
        env_file = ".env"


settings = Settings()

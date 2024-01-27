from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    CLIENT_SECRET: str
    USER_AGENT: str
    CLIENT_ID: str
    KAFKA_HOST: str
    KAFKA_PORT: int

    class Config:
        env_file = ".env"


settings = Settings()

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    CLIENT_SECRET: str
    USER_AGENT: str
    CLIENT_ID: str
    KAFKA_HOST: str
    KAFKA_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_PORT: int
    DB_HOST: str
    DB_DATABASE: str
    MONGO_ROOT_USERNAME: str
    MONGO_ROOT_PASSWORD: str

    class Config:
        env_file = ".env"


settings = Settings()

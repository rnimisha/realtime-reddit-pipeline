from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_KEY: str
    API_KEY_SECRET: str
    ACCESS_TOKEN: str
    ACCESS_TOKEN_SECRET: str

    class Config:
        env_file = ".env"


settings = Settings()

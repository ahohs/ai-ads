from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Ads"
    version: str = "0.1.0"
    app_env: str = "dev"
    cors_origins: str = "*"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

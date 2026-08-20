from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Lead Management API"
    app_env: str = "development"
    database_url: str
    secret_key: str
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 20

    class Config:
        env_file = ".env"


settings = Settings()

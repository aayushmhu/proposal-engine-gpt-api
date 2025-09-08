from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_ENV: str = "dev"
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-3.5-turbo"
    DB_URI: str = "sqlite:///./dev.db"
    MAX_PROMPT_TOKENS: int = 60000

    class Config:
        env_file = ".env"

settings = Settings()

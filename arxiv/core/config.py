from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env',extra="ignore")
    arxiv_api_url: str = "https://export.arxiv.org/api/query"

settings = Settings()
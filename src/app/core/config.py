from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FastAPI Starter"
    debug: bool = False

    log_level: str = "INFO"
    log_to_file: bool = False
    log_file_path: str = "logs/app.log"


    chat_model_provider_url : str = "https://inference.jhingaai.com/v1"
    chat_model_name : str = "gpt-oss:20b"


    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()

from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = 'localhost'
    server_port: int = 8001

    max_note_title_length: int = 30
    max_note_text_length: int = 500

    username_max_length: int = 30
    username_min_length: int = 5

    password_min_length: int = 8
    password_max_length: int = 30


settings = Settings()

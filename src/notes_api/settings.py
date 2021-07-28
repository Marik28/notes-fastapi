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

    postgres_username: str
    postgres_password: str
    postgres_db_name: str
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    jwt_secret: str


settings = Settings()
DATABASE_URL = f"postgresql://{settings.postgres_username}:" \
               f"{settings.postgres_password}" \
               f"@{settings.postgres_host}:" \
               f"{settings.postgres_port}/" \
               f"{settings.postgres_db_name}"

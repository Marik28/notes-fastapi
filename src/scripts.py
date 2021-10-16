import typer

app = typer.Typer()


@app.command()
def create_tables():
    from notes_api.database import engine
    from notes_api.tables import Base
    from notes_api.settings import settings
    Base.metadata.create_all(engine)
    typer.echo(f"Таблицы в БД {settings.postgres_db_name} успешно созданы")


@app.command()
def create_jwt_secret(token_length: int = typer.Argument(32)):
    import secrets
    typer.echo(f"Токен сгенерирован:\n{secrets.token_urlsafe(token_length)}")


if __name__ == '__main__':
    app()

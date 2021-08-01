import argparse


def create_tables():
    from notes_api.database import engine
    from notes_api.tables import Base
    from notes_api.settings import settings
    Base.metadata.create_all(engine)
    print(f"Таблицы в БД {settings.postgres_db_name} успешно созданы")


def create_jwt_secret():
    import secrets
    print(secrets.token_urlsafe(32))


available_commands = ["create-tables", "create-jwt-secret"]
parser = argparse.ArgumentParser()
parser.add_argument("command", help="Команда, которую необходимо выполнить", choices=available_commands)

command_to_function = {
    "create-tables": create_tables,
    "create-jwt-secret": create_jwt_secret,
}

if __name__ == '__main__':
    args = parser.parse_args()
    print(args.command)
    command_to_function[args.command]()

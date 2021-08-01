import argparse


def create_tables():
    from notes_api.database import engine
    from notes_api.tables import Base
    from notes_api.settings import settings
    Base.metadata.create_all(engine)
    print(f"Таблицы в БД {settings.postgres_db_name} успешно созданы")


available_commands = ["create_tables"]
parser = argparse.ArgumentParser()
parser.add_argument("command", help="Команда, которую необходимо выполнить", choices=available_commands)

command_to_function = {
    "create_tables": create_tables,
}

if __name__ == '__main__':
    args = parser.parse_args()
    print(args.command)
    command_to_function[args.command]()

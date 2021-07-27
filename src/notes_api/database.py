from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()

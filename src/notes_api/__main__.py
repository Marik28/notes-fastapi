import uvicorn

from .database import engine
from .tables import Base

Base.metadata.create_all(engine)
uvicorn.run("notes_api.app:app")

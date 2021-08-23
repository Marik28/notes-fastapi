from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import router
from .settings import settings

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import FastAPI

from app.core.config import settings
from app.api.v1 import api

app = FastAPI()
app.include_router(api.router, prefix=settings.API_PREFIX)

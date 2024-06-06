from fastapi import FastAPI
from routes.routes import abc

apps = FastAPI()

apps.include_router(abc)
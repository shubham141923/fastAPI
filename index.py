from fastapi import FastAPI
from routes.routes import routes

app = FastAPI()

app.include_router(routes)
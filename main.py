from api import router
from utils.services import get_service_details
from fastapi import FastAPI

app = FastAPI(**get_service_details())

app.include_router(router)
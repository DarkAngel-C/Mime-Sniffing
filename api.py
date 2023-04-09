from loguru import logger
from fastapi import APIRouter, UploadFile, Query
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get(
    "/",
    tags=["Greetings"],
    summary="Greet the user",
)
async def greet():
    logger.info("Greeted")
    return "Hello User !"


@router.post(
    "/doc",
    tags=["Upload"],
    summary="Upload a document",
)
async def upload_doc(_file: UploadFile = Query(...)):
    return JSONResponse(content="File uploaded", headers={"Content-Type": ""})

@router.post(
    "/comment",
    tags=["Comment"],
    summary="Comment on a document"
)
async def comment(cmnt):
    return JSONResponse(content="Commented", headers={"Content-Type": ""})
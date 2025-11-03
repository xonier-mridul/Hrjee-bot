from fastapi import FastAPI, APIRouter, Response, Body

from app.controllers.query_controller import handle_incoming_prompt
from app.validationSchemas.query_validation_schema import promt_schema

router = APIRouter()



@router.post('/')
async def handle_prompt(response: Response, content: promt_schema):
    return await handle_incoming_prompt( response, content.model_dump())
from fastapi import APIRouter, Request

from app.api.v1.services.response_service import ResponseService

router = APIRouter()

response_service = ResponseService()


@router.get("/")
def get_hello_world(request: Request):
    return response_service.to_response(
        request,
        {'result': 'Hello world!'},
    )

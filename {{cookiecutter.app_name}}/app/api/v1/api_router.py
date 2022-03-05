from fastapi import APIRouter

from app.api.v1.endpoints import hello_word

router = APIRouter()

# Sample router
# router.include_router(login.router, tags=["login"])
# router.include_router(hello_word.router, prefix="/foo", tags=["foo"])

router.include_router(hello_word.router, tags=["hello_world"])

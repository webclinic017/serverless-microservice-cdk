from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def get_cart():
    return {"message": "cart"}
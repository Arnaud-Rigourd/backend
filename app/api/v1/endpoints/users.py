from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import user as crud_user
from app.db.dependencies import get_db
from app.schemas.user import User, UserCreate

router = APIRouter()


@router.post("/", response_model=User)
async def create_user(
    *,
    db: AsyncSession = Depends(get_db),
    user_in: UserCreate,
):
    """
    Create a new user.
    """
    user = await crud_user.create_user(db=db, user_in=user_in)
    return user

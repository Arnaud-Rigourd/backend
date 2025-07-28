from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.schemas.user import UserCreate


async def create_user(db: AsyncSession, *, user_in: UserCreate) -> User:
    # In a real app, you'd hash the password here.
    fake_hashed_password = user_in.password + "notreallyhashed"
    db_user = User(
        email=user_in.email, hashed_password=fake_hashed_password
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

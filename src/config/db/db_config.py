from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SYNCHRONOUS SQLALCHEMY
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:password@192.168.9.79/fastapi"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future = True)

Base = declarative_base()
# DB Utilities
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ASYNCHRONOUS SQLALCHEMY
ASYNC_SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:password@192.168.9.79/fastapi"
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
AsyncSessionLocal = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
# DB Utilities
async def async_get_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 資料庫 URL (這裡假設使用的是 SQLite，可以根據你的需求更改)
SQLALCHEMY_DATABASE_URL = "sqlite:///./smart_calendar.db"

# 建立資料庫引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 建立會話 (Session)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 宣告基底類別
Base = declarative_base()

# 提供資料庫會話的依賴項 (FastAPI Dependency Injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
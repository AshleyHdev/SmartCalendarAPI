from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os
from app.models import schedule  # 引入你的資料表模型

# 這個是你的資料庫 URL 設定
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:new_password@localhost/smart_calendar")

# 這個是 Alembic 設定檔的設定物件
config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# 設定日誌檔
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 這裡告訴 Alembic 你的資料表模型在哪
from app.models import schedule  # 引入你的資料表模型
target_metadata = schedule.Base.metadata

# 建立資料庫引擎
def run_migrations_offline():
    """在離線模式下運行"""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """在連線模式下運行"""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

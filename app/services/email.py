from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.config import settings
from pydantic import EmailStr
from typing import List
import asyncio


# 設定 Email 連線配置
conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,   # 啟用 TLS
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,     # 啟用 SSL
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

# 發送 Email 的非同步函式
async def send_email(subject: str, email_to: List[EmailStr], body: str):
    message = MessageSchema(
        subject=subject,
        recipients=email_to,
        body=body,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)

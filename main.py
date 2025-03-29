import asyncio  # 確認這個有 import
from fastapi import FastAPI, BackgroundTasks, Depends, HTTPException
from app.api.routes import schedule  # 引入行程管理的 API
from app.services.email import send_email  # 引入 Email 發送功能
from pydantic import BaseModel, EmailStr
from typing import List

# 初始化 FastAPI 應用
app = FastAPI(
    title="Smart Calendar API",
    description="這是用來管理行程的 API 專案，支援 Email 傳送功能",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 根目錄測試路由
@app.get("/")
def read_root():
    return {"message": "歡迎來到 Smart Calendar API！這裡會變成最強的行事曆 API！💗"}

# 將行程管理的路由註冊到 FastAPI 應用中
app.include_router(schedule.router)

# ===================
# 📧 原本的發送 Email 功能 (Query Parameter)
# ===================
@app.post("/send-email/")
async def email_endpoint(background_tasks: BackgroundTasks, email_to: str):
    subject = "這是來自 Smart Calendar API 的測試郵件"
    body = "<h1>測試成功！</h1><p>你的 API 已經可以發送 Email 了！</p>"
    background_tasks.add_task(send_email, subject, [email_to], body)
    return {"message": "Email 已送出！（Query 版本）"}

# ===================
# 📧 新增的發送 Email 功能 (Request Body)
# ===================
class EmailSchema(BaseModel):
    subject: str
    email_to: List[EmailStr]
    body: str

@app.post("/send-email-body/")
async def send_email_with_body(background_tasks: BackgroundTasks, email_request: EmailSchema):  # 修改這一行！
    task = asyncio.create_task(send_email(
        subject=email_request.subject,
        email_to=email_request.email_to,
        body=email_request.body
    ))
    background_tasks.add_task(task)
    return {"message": "自訂 Email 已送出！"}

from fastapi import FastAPI, BackgroundTasks
from app.services.email import send_email
from app.api.routes import schedule  # 不要忘了引入行程 API 路由

app = FastAPI(
    title="Smart Calendar API",
    description="這是用來管理行程的 API 專案，支援 Email 傳送功能",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 加入行程 API 路由
app.include_router(schedule.router)

@app.get("/")
def read_root():
    return {"message": "歡迎來到 Smart Calendar API！這裡會變成最強的行事曆 API！💗"}

# 發送 Email 測試 API
@app.post("/send-email/")
async def email_endpoint(background_tasks: BackgroundTasks, email_to: str):
    subject = "這是來自 Smart Calendar API 的測試郵件"
    body = "<h1>測試成功！</h1><p>你的 API 已經可以發送 Email 了！</p>"
    background_tasks.add_task(send_email, subject, [email_to], body)
    return {"message": "Email 已送出！"}
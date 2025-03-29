# SmartCalendarAPI

SmartCalendarAPI is a powerful and intelligent calendar management system built using **FastAPI** and **SQLAlchemy**. It provides robust scheduling features and supports automated email notifications for calendar events. This project aims to offer a high-quality scheduling API that can be further enhanced with various features in the future.

## Features
- 📅 **Schedule Management:**
  - Create, update, delete, and retrieve scheduled events.
  - Supports adding details like title, description, date, and time.
  
- ✉️ **Email Notifications:**
  - Automatically sends calendar event summaries and notifications via email.
  - Designed to handle asynchronous email sending with background tasks.

## Technologies Used
- **FastAPI** - High-performance web framework for building APIs.
- **SQLAlchemy** - ORM (Object-Relational Mapping) for handling database operations.
- **Alembic** - Database migration tool for handling schema changes.
- **PostgreSQL** - Relational database used for storing schedules.
- **Python-dotenv** - For managing environment variables.
- **Pydantic** - Data validation and serialization.
- **FastAPI-Mail** - For handling email configuration and sending.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/AshleyHdev/SmartCalendarAPI.git
```

2. Navigate to the project directory:
```bash
cd SmartCalendarAPI
```

3. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the root directory and add your email configuration:
```
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
MAIL_FROM=your_email@gmail.com
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIL_STARTTLS=True
MAIL_SSL_TLS=False
```

6. Run the database migrations:
```bash
alembic upgrade head
```

7. Run the FastAPI application:
```bash
uvicorn app.main:app --reload
```

## Usage
The API documentation is available at:
```
http://127.0.0.1:8000/docs
```

### Example API Requests
#### 1. Create a Schedule
```http
POST /api/schedules/
```
```json
{
  "title": "Team Meeting",
  "description": "Discuss project progress",
  "date": "2025-03-29",
  "time": "14:00"
}
```

#### 2. Send Email Notification
```http
POST /send-email-body/
```
```json
{
  "subject": "Meeting Reminder",
  "email_to": ["example@gmail.com"],
  "body": "Don't forget about our meeting at 14:00."
}
```

## Future Improvements
- ✅ Adding **AI-based schedule analysis** to provide smart suggestions.
- ✅ Support for **CSV/Excel file import and export**.
- ✅ Google Calendar synchronization (Coming Soon).

# Smart Calendar API 專案 (中文版)

這是一個使用 FastAPI 和 PostgreSQL 建立的行事曆 API 專案，支援行程管理與 Email 傳送功能。這個專案展示了基本的 RESTful API 設計，以及如何透過 FastAPI 處理資料庫操作與背景任務。

## 專案功能
- 📅 **行程管理功能**：
  - 建立、讀取、更新、刪除 (CRUD) 行程資料。
  - 支援 SQLAlchemy ORM 與 PostgreSQL 資料庫。

- 📧 **Email 傳送功能**：
  - 可透過 FastAPI 的背景任務功能 (BackgroundTasks) 傳送 Email。
  - 支援同步與非同步的 Email 發送。

- 📝 **專案架構 (檔案結構)**：
```bash
SmartCalendarAPI/
│
├── app/
│   ├── api/                 # 路由 (包含行程相關的 API)
│   ├── models/              # 資料庫模型
│   ├── schemas/             # Pydantic 模式 (Schema)
│   ├── services/            # Email 傳送與行程處理功能
│   ├── config.py            # 設定檔 (包含 Email 設定)
│   ├── database.py          # 資料庫初始化
│   ├── main.py              # FastAPI 主檔案
│
├── requirements.txt        # 相依套件列表
├── README.md               # 專案說明檔案 (這個檔案！)
├── Dockerfile              # Docker 部署設定
```

## 如何啟動專案
1. 克隆這個專案：
```bash
 git clone https://github.com/AshleyHdev/SmartCalendarAPI.git
```

2. 進入專案資料夾並建立虛擬環境：
```bash
cd SmartCalendarAPI
python3 -m venv venv
source venv/bin/activate
```

3. 安裝相依套件：
```bash
pip install -r requirements.txt
```

4. 設定環境變數 (.env 檔案)：
```
MAIL_USERNAME=你的Gmail帳號
MAIL_PASSWORD=你的Gmail應用程式密碼
MAIL_FROM=你的Gmail帳號
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIL_STARTTLS=True
MAIL_SSL_TLS=False
```

5. 啟動專案：
```bash
uvicorn app.main:app --reload
```

6. 開啟瀏覽器檢視 API 文件：
```
http://127.0.0.1:8000/docs
```

## 未來規劃
- ✅ 增加更多行程管理功能。
- ✅ 增加 Email 傳送的自訂化功能。
- 📌 優化系統效能與安全性。

## 授權
本專案使用 MIT 授權條款，詳情請見 LICENSE 檔案。

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
**AshleyH.dev**

Enjoy building the most powerful Smart Calendar API! 💪💗

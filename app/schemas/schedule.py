from pydantic import BaseModel, Field

class ScheduleBase(BaseModel):
    title: str = Field(..., title="行程標題", description="行程的標題名稱")
    description: str = Field(..., title="行程描述", description="對行程的詳細說明")
    date: str = Field(..., title="行程日期", description="行程的日期 (格式：YYYY-MM-DD)")
    time: str = Field(..., title="行程時間", description="行程的時間 (格式：HH:MM)")

class ScheduleCreate(ScheduleBase):
    """
    用於建立行程的 Schema，不包含行程的 ID。
    """
    pass

class ScheduleUpdate(ScheduleBase):
    """
    用於更新行程的 Schema，允許更新行程的標題、描述、日期和時間。
    """
    pass

class Schedule(ScheduleBase):
    id: int = Field(..., title="行程 ID", description="資料庫中自動生成的行程 ID")

    class Config:
        from_attributes = True  # 這是 Pydantic V2 替代 orm_mode 的寫法
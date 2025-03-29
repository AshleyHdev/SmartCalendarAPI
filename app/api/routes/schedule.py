from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import schedule  # 導入剛才移動的檔案
from app.schemas.schedule import ScheduleCreate, ScheduleUpdate
from app.database import get_db  # 確定你的 get_db 是這樣命名

router = APIRouter()

@router.post("/schedules/")
def create_new_schedule(schedule_data: ScheduleCreate, db: Session = Depends(get_db)):
    return schedule.create_schedule(db, schedule_data)

@router.get("/schedules/{schedule_id}")
def read_schedule(schedule_id: int, db: Session = Depends(get_db)):
    db_schedule = schedule.get_schedule(db, schedule_id)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return db_schedule

@router.get("/schedules/")
def read_all_schedules(db: Session = Depends(get_db)):
    return schedule.get_all_schedules(db)

@router.put("/schedules/{schedule_id}")
def update_existing_schedule(schedule_id: int, schedule_data: ScheduleUpdate, db: Session = Depends(get_db)):
    db_schedule = schedule.update_schedule(db, schedule_id, schedule_data)
    if db_schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return db_schedule

@router.delete("/schedules/{schedule_id}")
def delete_existing_schedule(schedule_id: int, db: Session = Depends(get_db)):
    return schedule.delete_schedule(db, schedule_id)

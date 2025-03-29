from sqlalchemy.orm import Session
from app.models.schedule import Schedule
from app.schemas.schedule import ScheduleCreate, ScheduleUpdate
from fastapi import APIRouter


def create_schedule(db: Session, schedule: ScheduleCreate):
    db_schedule = Schedule(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return {
        "id": db_schedule.id,
        "title": db_schedule.title,
        "description": db_schedule.description,
        "date": db_schedule.date,
        "time": db_schedule.time
    }

def get_schedule(db: Session, schedule_id: int):
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if db_schedule:
        return {
            "id": db_schedule.id,
            "title": db_schedule.title,
            "description": db_schedule.description,
            "date": db_schedule.date,
            "time": db_schedule.time
        }
    return None

def get_all_schedules(db: Session):
    # 這個函式要確保所有行程都被返回
    schedules = db.query(Schedule).all()
    return [
        {
            "id": schedule.id,
            "title": schedule.title,
            "description": schedule.description,
            "date": schedule.date,
            "time": schedule.time
        } for schedule in schedules
    ]

def update_schedule(db: Session, schedule_id: int, schedule: ScheduleUpdate):
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if db_schedule:
        for key, value in schedule.dict().items():
            setattr(db_schedule, key, value)
        db.commit()
        db.refresh(db_schedule)
        return {
            "id": db_schedule.id,
            "title": db_schedule.title,
            "description": db_schedule.description,
            "date": db_schedule.date,
            "time": db_schedule.time
        }
    return None

def delete_schedule(db: Session, schedule_id: int):
    db_schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if db_schedule:
        db.delete(db_schedule)
        db.commit()
        return {"message": "Schedule deleted successfully"}
    return {"message": "Schedule not found"}
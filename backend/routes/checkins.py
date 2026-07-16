"""
Endpoints for marking a habit done on a given day, and reading check-in
history (used to build streaks/charts on the frontend).
"""
from fastapi import APIRouter, Header
from datetime import date
from database import supabase
from models.schemas import CheckinCreate
from routes.habits import get_user_id

router = APIRouter(prefix="/checkins", tags=["checkins"])


@router.post("/")
def create_checkin(checkin: CheckinCreate, authorization: str = Header(...)):
    user_id = get_user_id(authorization)
    payload = {
        "habit_id": checkin.habit_id,
        "user_id": user_id,
        "checkin_date": str(checkin.checkin_date or date.today()),
    }
    result = supabase.table("habit_checkins").insert(payload).execute()
    return result.data[0]


@router.get("/{habit_id}")
def get_checkins(habit_id: str, authorization: str = Header(...)):
    user_id = get_user_id(authorization)
    result = (
        supabase.table("habit_checkins")
        .select("*")
        .eq("habit_id", habit_id)
        .eq("user_id", user_id)
        .execute()
    )
    return result.data

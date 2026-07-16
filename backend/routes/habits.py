"""
All endpoints related to creating, listing, and deleting habits.
Check-ins (marking a habit done for a day) live in checkins.py, kept separate
so this file stays focused only on habit management.
"""
from fastapi import APIRouter, HTTPException, Header
from database import supabase
from models.schemas import HabitCreate

router = APIRouter(prefix="/habits", tags=["habits"])


def get_user_id(authorization: str = Header(...)) -> str:
    """Extract the user id from the Supabase auth token sent by the frontend."""
    token = authorization.replace("Bearer ", "")
    user = supabase.auth.get_user(token)
    if not user or not user.user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user.user.id


@router.get("/")
def list_habits(authorization: str = Header(...)):
    user_id = get_user_id(authorization)
    result = supabase.table("habits").select("*").eq("user_id", user_id).execute()
    return result.data


@router.post("/")
def create_habit(habit: HabitCreate, authorization: str = Header(...)):
    user_id = get_user_id(authorization)
    payload = habit.model_dump()
    payload["user_id"] = user_id
    result = supabase.table("habits").insert(payload).execute()
    return result.data[0]


@router.delete("/{habit_id}")
def delete_habit(habit_id: str, authorization: str = Header(...)):
    user_id = get_user_id(authorization)
    supabase.table("habits").delete().eq("id", habit_id).eq("user_id", user_id).execute()
    return {"status": "deleted"}

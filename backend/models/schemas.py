"""
Data models (request/response shapes) for the habit tracker API.
Keeping these separate from routes keeps each file focused on one job.
"""
from pydantic import BaseModel
from typing import Optional
from datetime import date


class HabitCreate(BaseModel):
    name: str
    description: Optional[str] = None
    color: Optional[str] = "#4F46E5"
    target_frequency: Optional[str] = "daily"


class HabitResponse(BaseModel):
    id: str
    name: str
    description: Optional[str]
    color: str
    target_frequency: str
    created_at: str


class CheckinCreate(BaseModel):
    habit_id: str
    checkin_date: Optional[date] = None  # defaults to today if not provided

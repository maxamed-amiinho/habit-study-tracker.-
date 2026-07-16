"""
Main entry point for the Habit Tracker API.
Run locally with: uvicorn app:app --reload
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.habits import router as habits_router
from routes.checkins import router as checkins_router

app = FastAPI(title="Habit Tracker API")

# Allow the frontend (served from anywhere during development, and from
# your deployed domain in production) to call this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten this to your real frontend URL once deployed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(habits_router)
app.include_router(checkins_router)


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Habit Tracker API is running"}

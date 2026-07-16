/**
 * Central place for all calls to the backend API.
 * Every other frontend file talks to the backend only through these functions.
 */

// Change this to your deployed Railway URL once the backend is live.
const API_BASE_URL = "http://localhost:8000";

function getAuthToken() {
  return localStorage.getItem("supabase_token");
}

async function apiRequest(path, options = {}) {
  const token = getAuthToken();
  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...options.headers,
    },
  });

  if (!response.ok) {
    const errorBody = await response.json().catch(() => ({}));
    throw new Error(errorBody.detail || `Request failed: ${response.status}`);
  }
  return response.json();
}

export function getHabits() {
  return apiRequest("/habits/");
}

export function createHabit(habit) {
  return apiRequest("/habits/", {
    method: "POST",
    body: JSON.stringify(habit),
  });
}

export function deleteHabit(habitId) {
  return apiRequest(`/habits/${habitId}`, { method: "DELETE" });
}

export function createCheckin(habitId, checkinDate) {
  return apiRequest("/checkins/", {
    method: "POST",
    body: JSON.stringify({ habit_id: habitId, checkin_date: checkinDate }),
  });
}

export function getCheckins(habitId) {
  return apiRequest(`/checkins/${habitId}`);
}

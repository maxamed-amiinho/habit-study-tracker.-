/**
 * Renders a single habit as a card: name, color accent, a "mark done today"
 * button, and its current streak count.
 */
import { createCheckin, getCheckins } from "../utils/api.js";

export async function renderHabitCard(habit, onChange) {
  const card = document.createElement("div");
  card.className = "habit-card";
  card.style.borderLeftColor = habit.color;

  const checkins = await getCheckins(habit.id);
  const streak = calculateStreak(checkins);

  card.innerHTML = `
    <div class="habit-card-header">
      <h3>${habit.name}</h3>
      <span class="streak-badge">🔥 ${streak} day streak</span>
    </div>
    <p class="habit-description">${habit.description || ""}</p>
    <button class="checkin-btn">Mark done today</button>
  `;

  card.querySelector(".checkin-btn").addEventListener("click", async () => {
    await createCheckin(habit.id);
    onChange();
  });

  return card;
}

function calculateStreak(checkins) {
  if (!checkins.length) return 0;
  const dates = checkins.map((c) => c.checkin_date).sort().reverse();
  let streak = 1;
  for (let i = 0; i < dates.length - 1; i++) {
    const current = new Date(dates[i]);
    const prev = new Date(dates[i + 1]);
    const dayDiff = (current - prev) / (1000 * 60 * 60 * 24);
    if (dayDiff === 1) {
      streak++;
    } else {
      break;
    }
  }
  return streak;
}

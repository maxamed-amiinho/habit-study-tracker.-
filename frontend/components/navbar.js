/**
 * Simple top navbar used on every page. Shows the app name and a
 * logout button when the user is logged in.
 */
import { signOut } from "../utils/auth.js";

export function renderNavbar() {
  const nav = document.createElement("nav");
  nav.className = "navbar";
  nav.innerHTML = `
    <span class="navbar-title">Habit Tracker</span>
    <button class="logout-btn">Log out</button>
  `;
  nav.querySelector(".logout-btn").addEventListener("click", async () => {
    await signOut();
    window.location.href = "login.html";
  });
  return nav;
}

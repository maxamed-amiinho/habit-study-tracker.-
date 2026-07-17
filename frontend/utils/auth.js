/**
 * Handles login/signup directly against Supabase Auth from the browser.
 * The resulting token is stored and then sent to our backend on every
 * request (see api.js) so the backend knows which user is calling it.
 */
import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm";

const SUPABASE_URL = "https://ituyokmsllgkomzfqwnd.supabase.co";
const SUPABASE_ANON_KEY = "sb_publishable_VKtU_k78b6bEP4miB5-Otw_V95i1VrZ";

export const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

export async function signUp(email, password) {
  const { data, error } = await supabase.auth.signUp({ email, password });
  if (error) throw error;
  return data;
}

export async function signIn(email, password) {
  const { data, error } = await supabase.auth.signInWithPassword({ email, password });
  if (error) throw error;
  localStorage.setItem("supabase_token", data.session.access_token);
  return data;
}

export async function signOut() {
  await supabase.auth.signOut();
  localStorage.removeItem("supabase_token");
}

export function isLoggedIn() {
  return !!localStorage.getItem("supabase_token");
}

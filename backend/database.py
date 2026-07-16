"""
Supabase connection.
Reads credentials from environment variables (set these in Railway's dashboard,
and in a local .env file for testing on your own machine).
"""
import os
from supabase import create_client, Client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise RuntimeError(
        "Missing SUPABASE_URL or SUPABASE_KEY environment variables. "
        "Set them in Railway's Variables tab (and in a local .env file for testing)."
    )

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

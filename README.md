# Habit Tracker

A simple web app to track daily habits and streaks.

**Stack:** FastAPI (backend) + Supabase (database + auth) + plain HTML/CSS/JS (frontend)

## Project structure

```
habit-tracker/
├── backend/
│   ├── app.py              # FastAPI entry point
│   ├── database.py         # Supabase connection
│   ├── models/
│   │   └── schemas.py      # request/response data shapes
│   ├── routes/
│   │   ├── habits.py       # create/list/delete habits
│   │   └── checkins.py     # mark habits done, read history
│   └── requirements.txt
├── frontend/
│   ├── pages/               # login.html, signup.html, dashboard.html
│   ├── components/          # navbar.js, habit-card.js
│   ├── utils/                # api.js (backend calls), auth.js (Supabase auth)
│   └── styles/main.css
└── supabase/
    └── schema.sql            # run this in Supabase's SQL editor once
```

## 1. Set up Supabase

1. Create a project at supabase.com.
2. Open the SQL Editor and run `supabase/schema.sql`.
3. Go to Project Settings → API and copy your **Project URL** and **anon public key**.
4. Paste them into `frontend/utils/auth.js` (`SUPABASE_URL`, `SUPABASE_ANON_KEY`).

## 2. Run the backend locally

```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file in `backend/` (this is gitignored, never commit it):
```
SUPABASE_URL=https://YOUR-PROJECT.supabase.co
SUPABASE_KEY=your-anon-key
```

Then run:
```bash
uvicorn app:app --reload
```
The API will be live at `http://localhost:8000`.

## 3. Run the frontend locally

Just open `frontend/pages/login.html` in a browser, or serve the folder with:
```bash
cd frontend
python -m http.server 5500
```

## 4. Deploy

- **Backend → Railway**: connect your GitHub repo, set the root directory to `backend/`,
  add `SUPABASE_URL` and `SUPABASE_KEY` as environment variables in Railway's dashboard.
- **Frontend**: once the backend is deployed, update `API_BASE_URL` in
  `frontend/utils/api.js` to your Railway URL, then push the frontend folder
  to GitHub Pages, Netlify, or Vercel.

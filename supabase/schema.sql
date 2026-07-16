-- Habit Tracker Database Schema for Supabase
-- Run this in the Supabase SQL Editor (Project > SQL Editor > New Query)

-- Enable UUID generation
create extension if not exists "uuid-ossp";

-- Habits table: each habit a user wants to track
create table if not exists habits (
    id uuid primary key default uuid_generate_v4(),
    user_id uuid references auth.users(id) on delete cascade not null,
    name text not null,
    description text,
    color text default '#4F46E5',
    target_frequency text default 'daily', -- 'daily' or 'weekly'
    created_at timestamptz default now()
);

-- Check-ins table: one row per day a habit is marked complete
create table if not exists habit_checkins (
    id uuid primary key default uuid_generate_v4(),
    habit_id uuid references habits(id) on delete cascade not null,
    user_id uuid references auth.users(id) on delete cascade not null,
    checkin_date date not null default current_date,
    created_at timestamptz default now(),
    unique (habit_id, checkin_date) -- prevent duplicate check-ins same day
);

-- Indexes for faster queries
create index if not exists idx_habits_user_id on habits(user_id);
create index if not exists idx_checkins_habit_id on habit_checkins(habit_id);
create index if not exists idx_checkins_user_id on habit_checkins(user_id);
create index if not exists idx_checkins_date on habit_checkins(checkin_date);

-- Row Level Security: users can only see/edit their own data
alter table habits enable row level security;
alter table habit_checkins enable row level security;

create policy "Users can view their own habits"
    on habits for select using (auth.uid() = user_id);
create policy "Users can insert their own habits"
    on habits for insert with check (auth.uid() = user_id);
create policy "Users can update their own habits"
    on habits for update using (auth.uid() = user_id);
create policy "Users can delete their own habits"
    on habits for delete using (auth.uid() = user_id);

create policy "Users can view their own checkins"
    on habit_checkins for select using (auth.uid() = user_id);
create policy "Users can insert their own checkins"
    on habit_checkins for insert with check (auth.uid() = user_id);
create policy "Users can delete their own checkins"
    on habit_checkins for delete using (auth.uid() = user_id);

# Strategy Visualizer – Progress Tracker

> Rule: If it’s not in this file, it does not exist.

---

## Status Legend
- [ ] Not started
- [~] In progress
- [x] Done
- [!] Blocked
- [?] Needs clarification

---

## Current Focus (Max 3 items)
1. Backend – FastF1 session loader
2. Backend – Lap data normalization
3. Frontend – Strategy visualization skeleton

---

## Epics Overview

| Epic | Status | Notes |
|-----|-------|------|
| Backend – Data Acquisition | ⏳ | Foundation for everything |
| Backend – Strategy Engine | ⏸ | Depends on normalized laps |
| Backend – API Layer | ⏸ | Depends on strategy engine |
| Frontend – Core Visualization | ⏳ | Can run on mock data |
| Frontend – Animation & Interaction | ⏸ | After static viz |
| Testing & Validation | ⏸ | Epic-wise gates |

---

# EPIC 1: Backend – Data Acquisition

### EPIC GOAL
Load, cache, and normalize FastF1 session data in a deterministic and reusable way.

### Tasks
- [ ] Initialize FastAPI project structure
- [ ] Add FastF1 dependency and enable cache
- [~] Implement session loader function
  - [x] Accept season, round, session type
  - [ ] Validate season/round/session
  - [ ] Handle missing or unavailable sessions
- [ ] Extract race metadata (race name, circuit, total laps)
- [ ] Implement Redis or in-memory caching layer
- [ ] Centralize FastF1 access (no direct calls elsewhere)

### Testing Gate
- [ ] Can load at least 3 races without refetching
- [ ] Invalid season/round returns structured error
- [ ] Cached response time < 200ms

---

# EPIC 2: Backend – Strategy Engine

### EPIC GOAL
Derive accurate driver strategies (stints + pit stops) from lap-level data.

### Tasks
- [ ] Normalize lap dataframe
  - [ ] Sort laps by driver and lap number
  - [ ] Handle formation laps
  - [ ] Handle missing compound values
- [ ] Implement pit stop detection logic
- [ ] Implement stint segmentation logic
- [ ] Assign stint numbers per driver
- [ ] Compute stint lengths
- [ ] Aggregate driver-level strategy object
- [ ] Generate strategy pattern string (e.g. M → H → H)

### Testing Gate
- [ ] Stint count matches known race strategies
- [ ] Pit stop laps align with visual timing screens
- [ ] No overlapping or zero-length stints

---

# EPIC 3: Backend – API Layer

### EPIC GOAL
Expose clean, stable, and typed APIs for frontend consumption.

### Tasks
- [ ] Define Pydantic models for:
  - [ ] Stint
  - [ ] Strategy
  - [ ] Race metadata
- [ ] Implement race metadata endpoint
- [ ] Implement driver strategy endpoint
- [ ] Implement team strategy endpoint
- [ ] Implement multi-driver compare endpoint
- [ ] Add request validation and error handling
- [ ] Add OpenAPI documentation sanity check

### Testing Gate
- [ ] All endpoints return valid JSON schemas
- [ ] API works with both cached and uncached data
- [ ] Compare endpoint handles 1–N drivers

---

# EPIC 4: Frontend – Core Visualization

### EPIC GOAL
Render static race strategies as color-coded stint bars.

### Tasks
- [~] Initialize React + TypeScript project
- [ ] Define Strategy and Stint TypeScript types
- [ ] Create mock strategy JSON for development
- [ ] Implement main strategy chart container
- [ ] Implement X-axis lap scale
- [ ] Implement Y-axis driver rows
- [ ] Implement stint bar component
- [ ] Apply compound color mapping
- [ ] Render pit stop indicators

### Testing Gate
- [ ] Can render mock strategy without backend
- [ ] Colors match compound legend
- [ ] Layout supports 1–10 drivers cleanly

---

# EPIC 5: Frontend – Animation & Interaction

### EPIC GOAL
Animate strategy progression lap-by-lap with user controls.

### Tasks
- [ ] Implement lap slider control
- [ ] Implement play/pause controls
- [ ] Animate stint fill based on current lap
- [ ] Animate pit stop transitions
- [ ] Add tooltips for stints and pit stops
- [ ] Implement driver vs team selector tabs

### Testing Gate
- [ ] Animation deterministic for same lap input
- [ ] No visual glitches during lap transitions
- [ ] Controls responsive under rapid interaction

---

# EPIC 6: Testing & Validation

### EPIC GOAL
Validate correctness, performance, and reliability of the system.

### Tasks
- [ ] Validate strategies against real race examples
- [ ] Add backend unit tests for stint logic
- [ ] Add API integration tests
- [ ] Add frontend empty/error state handling
- [ ] Performance sanity check (cold vs cached)
- [ ] Final visual verification with multiple races

### Testing Gate
- [ ] No crashes on missing or partial data
- [ ] Strategy visuals match real F1 broadcasts
- [ ] Acceptable performance on mid-range laptop

---

# Ad-Hoc / Tech Debt / Discoveries

> Items discovered during implementation that need follow-up.

- [ ] FastF1 compound missing for specific laps
- [ ] Pit stop detection inconsistent for Lap 1
- [ ] Safety car laps affecting stint logic?
- [ ] Need compound legend redesign
- [ ] Consider precomputing strategies per race

---

# Notes & Decisions Log

- FastF1 cache enabled by default
- Frontend to use mock data until backend EPIC 3
- Strategy computation isolated in backend service layer

---

### How to use this effectively (quick reminder)

* Update this **daily** (2–5 minutes)
* Only move **3 items max** into *Current Focus*
* Never delete ad-hoc items — promote them instead
* Treat **Testing Gates** as hard stop conditions

If you want, next I can:

* Convert this into **GitHub Issues automatically**
* Define a **branching strategy per epic**
* Help you pick **charting + animation libraries** *before* you regret it 😄

Just say where you want to go next.

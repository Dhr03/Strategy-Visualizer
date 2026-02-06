# Strategy Visualizer (Tire + Pit Stops)

## **Requirements Document**


## 1. Project Overview

### 1.1 Purpose

Build a **Formula 1 race strategy visualizer** that reconstructs and displays **driver and team race strategies** (stints, tire compounds, pit stops) using **FastF1 data**, exposed via a **Python (FastAPI) backend** and rendered in a **React frontend** with animated, interactive visualizations.

### 1.2 Learning Goals

* Design **production-grade API contracts**
* Handle **data normalization + caching**
* Build **deterministic visualizations from time-series sports data**
* Practice **frontend animation + state synchronization**
* Separate **domain logic** from presentation logic

---

## 2. Tech Stack

### 2.1 Backend

* Python 3.11+
* FastAPI (async APIs)
* FastF1 (data source)
* Pandas (data processing)
* Redis (optional, recommended) — caching
* Pydantic — response schemas

### 2.2 Frontend

* React 18+
* TypeScript
* Charting: D3 / Recharts / Visx (decision deferred)
* State: React Query or Zustand
* Animation: CSS / Framer Motion

---

## 3. Core Domain Concepts (Explicit Definitions)

These definitions are **non-negotiable** and must be encoded in backend models.

### 3.1 Stint

A stint is defined as:

* Continuous laps driven by a driver
* With the same **tire compound**
* Between two pit stops (or race start/end)

### 3.2 Strategy

A strategy is:

* Ordered list of stints
* Associated pit stop laps
* Total laps completed

### 3.3 Tire Compound Canonical Mapping

| FastF1 Value | UI Label | Color  |
| ------------ | -------- | ------ |
| SOFT         | Soft     | Red    |
| MEDIUM       | Medium   | Yellow |
| HARD         | Hard     | White  |
| INTERMEDIATE | Inter    | Green  |
| WET          | Wet      | Blue   |

---

## 4. Functional Requirements (Backend)

### 4.1 Data Acquisition Layer

#### FR-BE-1: Session Loader

* Input:

  * `season`
  * `round`
  * `session_type` (`R`, `Q`, `FP1`, etc.)
* Behavior:

  * Load session using FastF1
  * Enable caching
* Failure handling:

  * Invalid round/session → 404
  * Missing data → structured error

#### FR-BE-2: Lap Data Extraction

* Extract:

  * Lap number
  * Driver code
  * Compound
  * PitInLap
  * PitOutLap
* Normalize missing compounds (e.g. formation laps)

---

### 4.2 Strategy Computation

#### FR-BE-3: Stint Detection Algorithm

For each driver:

1. Sort laps by lap number
2. Detect compound change OR pit stop
3. Create new stint object:

   * `start_lap`
   * `end_lap`
   * `compound`
   * `length`

#### FR-BE-4: Pit Stop Detection

* Pit stop lap = lap where:

  * `PitInLap == True`
* Store:

  * lap number
  * stint transition index

#### FR-BE-5: Strategy Aggregation

* Group stints per driver
* Compute:

  * Total stints
  * Total pit stops
  * Strategy pattern (e.g. `M → H → H`)

---

### 4.3 API Endpoints

#### FR-BE-6: Race Metadata Endpoint

```
GET /api/races/{season}/{round}
```

Returns:

* Race name
* Circuit
* Total laps
* Drivers list
* Teams list

#### FR-BE-7: Driver Strategy Endpoint

```
GET /api/strategies/driver
```

Query params:

* season
* round
* driver_code

Response:

```json
{
  "driver": "VER",
  "total_laps": 57,
  "stints": [
    {
      "stint_number": 1,
      "compound": "MEDIUM",
      "start_lap": 1,
      "end_lap": 14,
      "length": 14
    }
  ],
  "pit_stops": [14, 38]
}
```

#### FR-BE-8: Team Strategy Endpoint

```
GET /api/strategies/team
```

Returns strategies for both drivers

#### FR-BE-9: Multi-Driver Compare Endpoint

```
POST /api/strategies/compare
```

Body:

```json
{
  "drivers": ["HAM", "ALO", "VER"]
}
```

---

### 4.4 Performance & Caching

#### FR-BE-10: Session Cache

* Cache FastF1 session object by:

  * `season + round + session`
* TTL: configurable

#### FR-BE-11: Strategy Cache

* Cache computed strategies separately
* Avoid recomputation per request

---

## 5. Functional Requirements (Frontend)

### 5.1 Global UI Structure

#### FR-FE-1: Layout

* Header:

  * Race selector
  * Session selector
* Main panel:

  * Strategy visualization
* Side panel:

  * Driver / Team selector

---

### 5.2 Driver / Team Selection

#### FR-FE-2: Selection Tabs

* Tabs:

  * **Drivers**
  * **Teams**
* Driver mode:

  * Multi-select drivers
* Team mode:

  * Select team → auto-load both drivers

---

### 5.3 Strategy Visualization

#### FR-FE-3: Stint Bar Visualization

* X-axis: Lap number
* Y-axis: Driver rows
* Each stint:

  * Rectangular bar
  * Width = stint length
  * Color = compound

#### FR-FE-4: Pit Stop Indicators

* Vertical dashed line at pit stop lap
* Tooltip on hover:

  * Lap number
  * Transition compound

---

### 5.4 Animation

#### FR-FE-5: Lap-by-Lap Animation

* Play/Pause controls
* Slider:

  * Current lap
* As lap increases:

  * Stints partially fill
  * Pit stop triggers visual transition

#### FR-FE-6: Animation Sync Rules

* Animation must be:

  * Deterministic
  * Based only on lap number
* No time-based race assumptions

---

### 5.5 Color & Legend

#### FR-FE-7: Compound Legend

* Fixed position legend
* Compound → color mapping
* Hover highlights corresponding stints

---

## 6. Non-Functional Requirements

### 6.1 Performance

* Backend response time:

  * Cold load ≤ 3s
  * Cached ≤ 200ms
* Frontend render ≤ 16ms per frame during animation

### 6.2 Reliability

* Missing laps or pit data must not crash UI
* Backend must return empty stints gracefully

### 6.3 Maintainability

* Strategy logic isolated in:

  * `strategy_service.py`
* No FastF1 calls in API routers

---

## 7. Data Contracts (Strict)

### 7.1 Strategy DTO

```ts
type Stint = {
  stintNumber: number;
  compound: "SOFT" | "MEDIUM" | "HARD" | "INTERMEDIATE" | "WET";
  startLap: number;
  endLap: number;
  length: number;
};

type Strategy = {
  driver: string;
  team: string;
  totalLaps: number;
  stints: Stint[];
  pitStops: number[];
};
```

---

## 8. Atomic Task Breakdown (Implementation Roadmap)

### Backend Tasks

1. FastF1 session loader with caching
2. Lap dataframe normalizer
3. Stint segmentation function
4. Pit stop detection logic
5. Strategy aggregation service
6. API schema definitions
7. Driver strategy endpoint
8. Team strategy endpoint
9. Compare endpoint
10. Redis integration

### Frontend Tasks

1. Race selector UI
2. Driver/team selection UI
3. Stint bar renderer
4. Compound color mapping
5. Pit stop overlay renderer
6. Tooltip system
7. Animation controller
8. Lap slider + controls
9. API integration hooks
10. Error & empty state handling

---

## 9. Explicit Out-of-Scope (For v1)

* Strategy optimization or prediction
* Safety car detection
* Weather overlays
* Qualifying strategy

---

[[ 
    
Next possible steps:

* Design **exact stint detection pseudocode**
* Define **folder structure (backend + frontend)**
* Pick **D3 vs Recharts vs Visx** based on animation needs
* Turn this into **Jira-style tickets**

Just tell me the next step 👀

]]
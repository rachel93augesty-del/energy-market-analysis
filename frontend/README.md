# Brent Oil Market Analysis Dashboard

## Objective
Build an interactive dashboard to visualize Brent oil prices, explore historical trends, and analyze how key events affected the market. Stakeholders can filter data, highlight events, and drill down for insights.

---

## Project Structure

energy-market-analysis/
│
├─ backend/ # Flask backend
│ ├─ app.py # Main Flask app
│ ├─ routes.py # API endpoints
│ └─ data/ # Sample CSV or JSON data
│
├─ frontend_dash.py # Dash interactive dashboard
├─ requirements.txt # Python dependencies
└─ README.md # This file


---

## Setup Instructions

### 1. Clone the repository
```bash
git clone <https://github.com/rachel93augesty-del/energy-market-analysis>
cd energy-market-analysis
2. Create and activate a Python virtual environment
Windows:

python -m venv venv
venv\Scripts\activate
macOS/Linux:

python -m venv venv
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
Running the Application
Step 1: Start the Flask Backend
cd backend
python -m app
Runs at: http://127.0.0.1:5000

API Endpoints:
## Backend API Endpoints Documentation

The Flask backend provides the following endpoints for the Brent Oil Market Analysis Dashboard:

| Endpoint                 | Method | Description                                                                 | Response Example |
|--------------------------|--------|-----------------------------------------------------------------------------|-----------------|
| `/api/prices`            | GET    | Returns historical Brent oil price data.                                     | `[{"Date": "1987-05-20", "Price": 18.63}, ...]` |
| `/api/events`            | GET    | Returns historical events that impacted oil prices.                         | `[{"Date": "1990-08-02", "Event": "Iraq invades Kuwait - Oil Crisis"}, ...]` |
| `/api/change_points`     | GET    | Returns detected price change points (if implemented).                      | `[{"Date": "1987-10-16", "Change": "Significant increase"}, ...]` |

### Notes:
- All endpoints return data in JSON format.
- Dates are in `YYYY-MM-DD` format.
- Prices are in USD.
- If an endpoint is not implemented (e.g., change points), it will return an empty list `[]`.
- These endpoints are consumed by the frontend Dash/React application for visualization.

/api/prices → Historical Brent oil prices

/api/events → Key events impacting prices

/api/change_points → Detected change points 

Step 2: Start the Dash Frontend
cd ..
python frontend_dash.py
Dashboard available at: http://127.0.0.1:8050

Dashboard Features
Historical Trends: Interactive line chart of Brent oil prices over time

Event Impacts: Markers and lists for key events, highlighting price effects

KPIs: Average price, Maximum price, Minimum price, Price volatility (Std Dev)

Filters: Date range selectors for dynamic analysis

Responsive Layout: Desktop, tablet, and mobile-friendly

Dependencies
Backend (Flask): Flask, flask-cors, pandas, numpy

Frontend (Dash): dash, dash-bootstrap-components, plotly, pandas, requests

Install all dependencies with:

pip install -r requirements.txt
Notes
Always start the backend before the frontend.

Built for demonstration; Flask development server is not production-ready.

Dataset includes Brent oil prices (1987–2022) and historical events.
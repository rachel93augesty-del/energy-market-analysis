Brent Oil Market Change Point Analysis

Project Overview
This project analyzes Brent oil prices to detect and quantify the impact of geopolitical events, economic shocks, and OPEC policy changes using Bayesian Change Point Analysis. The goal is to provide data-driven insights for investors, policymakers, and energy companies.

Project Objectives

Identify key events that significantly affected Brent oil prices over the past decades.

Quantify structural changes in daily oil prices using Bayesian modeling.

Provide clear, actionable insights through visualizations and an interactive dashboard.

Project Structure
energy-market-analysis/
│
├── data/
│   ├── raw/                     # Original datasets (Brent prices)
│   ├── processed/               # Processed data (log returns, merged CSV)
│   └── events/                  # Key oil market events CSV
│
├── notebooks/                   # Jupyter notebooks for EDA, modeling, and analysis
├── src/                         # Reusable Python scripts for data loading, modeling, and analysis
├── dashboard/                   # Flask backend & React frontend for interactive visualizations
├── reports/                     # Interim and final reports
├── figures/                     # Plots, charts, and visual outputs
├── requirements.txt             # Python dependencies
└── README.md

Task Breakdown
Task 1: Data Analysis Workflow

Load Brent oil price data.

Perform exploratory data analysis (EDA) and visualize trends, volatility, and shocks.

Compile a CSV of 10–15 key geopolitical and economic events impacting oil markets.

Document assumptions, limitations, and analysis workflow.

Task 2: Bayesian Change Point Modeling

Build a PyMC-based Bayesian Change Point model to detect structural breaks.

Identify change points in price trends and quantify before/after impacts.

Associate detected change points with real-world events.

Produce probabilistic statements about impacts.

Task 3: Interactive Dashboard

Backend: Flask APIs serving historical prices, change points, and event correlations.

Frontend: React dashboard with interactive plots, event highlights, and date filtering.

Enables stakeholders to explore how key events influenced oil prices.

Usage

Open notebooks in notebooks/ to explore EDA, modeling, and event analysis.

Run Flask backend (dashboard/backend/app.py) to serve API endpoints.

Start React frontend (dashboard/frontend) to explore interactive dashboards.

Key Packages

pandas, numpy – data manipulation

matplotlib, seaborn – visualization

scipy – statistics

jupyter, jupyterlab – notebooks

PyMC – Bayesian modeling (Task 2)

Flask – backend API

React – frontend dashboard

Contributions

This project is part of the 10 Academy: Artificial Intelligence Mastery – Week 11 Challenge. Contributions follow GitHub best practices with branches for each task:

main → main branch

task-1 → Task 1: EDA & event dataset

task-2 → Task 2: Bayesian change point modeling

task-3 → Task 3: Dashboard development
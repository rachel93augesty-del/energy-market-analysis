# WORKFLOW_AND_ASSUMPTIONS.md

## Project: Change Point Analysis of Brent Oil Prices  
**Prepared by:** Rahel Aklog  
**Date:** 10 Feb 2026  

---

## 1. Project Objective

The objective of this project is to analyze how major geopolitical and economic events affect Brent oil prices using statistical and Bayesian change point modeling. The analysis supports investors, policymakers, and energy companies in understanding price dynamics, managing risks, and making data-driven decisions.

Key questions include:  
- Which events significantly impact Brent oil prices?  
- How can structural breaks in the time series be detected and quantified?  
- What insights can inform investment strategies, policy, and operational planning?

---

## 2. Data Overview

**Dataset:**  
- Historical Brent crude oil prices (May 20, 1987 – September 30, 2022)  
- Daily closing prices in USD per barrel  

**Event Data:**  
- 13+ major geopolitical, economic, and OPEC events affecting oil markets  
- Structured dataset with `Date` and `Event` columns  

**Derived Features:**  
- Log returns: `log(Price_t) - log(Price_{t-1})` to achieve stationarity  
- Volatility metrics and descriptive statistics  

---

## 3. Analysis Workflow

1. **Data Preparation & Cleaning**  
   - Load Brent price data and key events CSV  
   - Convert date columns to `datetime` format  
   - Inspect for missing or duplicate values  
   - Compute log returns for stationarity  

2. **Exploratory Data Analysis (EDA)**  
   - Visualize raw prices over time (trend and spikes)  
   - Compute descriptive statistics (mean, min, max, quantiles)  
   - Plot log returns to detect volatility clustering  
   - Overlay key events to visualize correlations with price movements  

3. **Time Series Properties Analysis**  
   - Trend Analysis: Identify long-term growth or decline in prices  
   - Stationarity Tests: ADF and KPSS to confirm log returns are stationary  
   - Volatility Patterns: Detect spikes corresponding to events or crises  

4. **Change Point Modeling (Bayesian Approach)**  
   - Define discrete uniform prior for switch point (τ)  
   - Model two regimes: before and after τ (mean ± variance)  
   - Use `pm.math.switch` to select parameters depending on τ  
   - Fit model using MCMC sampling (`pm.sample()`)  
   - Posterior analysis: identify probable change points, estimate regime-specific statistics, quantify impact  

5. **Event Association & Impact Quantification**  
   - Compare detected change points with researched events  
   - Formulate hypotheses for causal impact  
   - Quantify shifts in mean price and volatility (% change)  

6. **Documentation & Communication**  
   - Maintain clear, modular notebook code  
   - Generate plots, tables, and overlays of events  
   - Produce standalone workflow and assumptions document  
   - Prepare stakeholder-ready visuals for dashboards  

---

## 4. Assumptions

- Log returns are stationary and suitable for modeling  
- Major geopolitical/economic events affect oil prices  
- Missing or erroneous data points are minimal and handled via cleaning  
- Statistical correlations suggest potential impact but do not guarantee causation  
- Noise may introduce minor deviations in detected change points  
- Daily price granularity is sufficient for meaningful analysis  

---

## 5. Limitations

- Change points may not perfectly align with known events  
- Gradual trends may be under-detected if abrupt shifts are assumed  
- Extreme outliers may create false positives  
- Log returns approximate normality but may deviate in extreme events  
- Event dataset may not capture all impactful events  

---

## 6. Communication Plan

| Audience            | Channel / Medium                 | Purpose                                      | Frequency |
|--------------------|---------------------------------|---------------------------------------------|-----------|
| Investors           | PDF/Slide Deck, Jupyter Notebook | Present key events and price impacts       | One-time / On-demand |
| Policymakers        | Executive Summary, Charts        | Inform policy decisions on energy stability | One-time |
| Energy Companies    | Dashboard (React + Flask)        | Visualize price trends, volatility, change points | Interactive, real-time |
| Internal Team       | GitHub README, Slack             | Track workflow, assumptions, and updates   | Continuous |

**Visualization Strategy:**  
- Time series plots with event markers  
- Change point posterior distributions  
- Volatility clustering charts  
- Summary tables of pre- and post-change point statistics  

---

## 7. Next Steps

1. Finalize Bayesian change point model in PyMC  
2. Quantify change point impacts for all key events  
3. Build dashboard for stakeholder visualization  
4. Include additional macroeconomic data for extended analysis  
5. Update assumptions and limitations iteratively based on model performance  

---

## 8. Deliverables

- `notebooks/` → Jupyter notebook with full analysis  
- `data/events.csv` → structured key event dataset  
- `WORKFLOW_AND_ASSUMPTIONS.md` → this file  
- Dashboard → interactive, React + Flask visualization  
- Visualizations → plots saved in `/plots` for reports  

---

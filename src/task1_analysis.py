# src/task1_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# For stationarity tests
from statsmodels.tsa.stattools import adfuller, kpss

sns.set(style="whitegrid")

# -----------------------------
# 1. Load Data
# -----------------------------
def load_brent_prices(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # parse dates safely
    df = df.dropna(subset=['Date'])
    return df

def load_events(file_path: str) -> pd.DataFrame:
    import os
    if not os.path.exists(file_path):
        print(f"⚠️ Warning: Events file not found at {file_path}. Returning empty DataFrame.")
        return pd.DataFrame(columns=['Date', 'Event'])
    
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    return df

# -----------------------------
# 2. Exploratory Data Analysis
# -----------------------------
def plot_price_series(df):
    plt.figure(figsize=(14,6))
    plt.plot(df['Date'], df['Price'], color='blue', label='Brent Price')
    plt.title("Brent Oil Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_log_returns(df):
    plt.figure(figsize=(14,5))
    plt.plot(df['Date'][1:], df['Log_Returns'][1:], color='green', label='Log Returns')
    plt.title("Brent Oil Log Returns Over Time")
    plt.xlabel("Date")
    plt.ylabel("Log Return")
    plt.grid(True)
    plt.legend()
    plt.show()

def summary_statistics(df):
    stats = pd.DataFrame({
        'Price': df['Price'].describe(),
        'Log_Returns': df['Log_Returns'].describe()
    }).round(5)
    return stats

# -----------------------------
# 3. Stationarity Tests
# -----------------------------
def stationarity_tests(series, series_name="Series"):
    """
    Perform ADF and KPSS stationarity tests.
    """
    results = {}

    # ADF Test
    adf_test = adfuller(series.dropna(), autolag='AIC')
    results['ADF Statistic'] = adf_test[0]
    results['ADF p-value'] = adf_test[1]
    results['ADF Critical Values'] = adf_test[4]
    
    # KPSS Test
    kpss_test = kpss(series.dropna(), regression='c', nlags="auto")
    results['KPSS Statistic'] = kpss_test[0]
    results['KPSS p-value'] = kpss_test[1]
    results['KPSS Critical Values'] = kpss_test[3]

    print(f"\n📌 Stationarity Test Results for {series_name}:")
    print(f"ADF Statistic: {results['ADF Statistic']:.5f}, p-value: {results['ADF p-value']:.5f}")
    print(f"KPSS Statistic: {results['KPSS Statistic']:.5f}, p-value: {results['KPSS p-value']:.5f}")
    print(f"ADF Critical Values: {results['ADF Critical Values']}")
    print(f"KPSS Critical Values: {results['KPSS Critical Values']}")
    
    return results

# src/task1_analysis.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# -----------------------------
# 1. Load Data
# -----------------------------

def load_brent_prices(file_path: str) -> pd.DataFrame:
    """
    Load Brent oil price CSV and parse dates.
    """
    df = pd.read_csv(file_path)
    # Specify exact date format to avoid warnings
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y', errors='coerce')  
    # Optional: remove rows where date parsing failed
    df = df.dropna(subset=['Date'])
    return df


def load_events(file_path: str) -> pd.DataFrame:
    """
    Load key oil market events CSV.
    """
    import pandas as pd
    import os

    if not os.path.exists(file_path):
        print(f"⚠️ Warning: Events file not found at {file_path}. Returning empty DataFrame.")
        return pd.DataFrame(columns=['Date', 'Event'])

    # Read CSV
    df = pd.read_csv(file_path)

    # Convert 'Date' column to datetime, auto-infer format
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
    else:
        print("⚠️ Warning: 'Date' column not found in events CSV.")
        df['Date'] = pd.NaT

    return df


# -----------------------------
# 2. Exploratory Data Analysis
# -----------------------------
def plot_price_series(df, title="Brent Oil Prices"):
    plt.figure(figsize=(14,6))
    plt.plot(df['Date'], df['Price'], label='Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title(title)
    plt.legend()
    plt.show()

def plot_log_returns(df, column='Price', title="Log Returns"):
    df['LogReturn'] = np.log(df[column]) - np.log(df[column].shift(1))
    plt.figure(figsize=(14,6))
    plt.plot(df['Date'], df['LogReturn'], label='Log Return', color='orange')
    plt.xlabel('Date')
    plt.ylabel('Log Return')
    plt.title(title)
    plt.legend()
    plt.show()

# -----------------------------
# 3. Basic Statistics
# -----------------------------
def summary_statistics(df, column='Price'):
    stats = {
        'Min': df[column].min(),
        'Max': df[column].max(),
        'Mean': df[column].mean(),
        'Median': df[column].median(),
        'Std': df[column].std(),
        '25th Percentile': df[column].quantile(0.25),
        '50th Percentile': df[column].quantile(0.5),
        '75th Percentile': df[column].quantile(0.75)
    }
    return stats

# -----------------------------
# 4. Main execution for notebook
# -----------------------------
if __name__ == "__main__":
    # File paths
    brent_file = '../data/raw/BrentOilPrices.csv'
    events_file = '../data/events/key_oil_market_events.csv'

    # Load data
    brent_df = load_brent_prices(brent_file)
    events_df = load_events(events_file)

    # Print head
    print(brent_df.head())
    print(events_df.head())

    # Plot price and returns
    plot_price_series(brent_df)
    plot_log_returns(brent_df)

    # Print summary stats
    stats = summary_statistics(brent_df)
    for k,v in stats.items():
        print(f"{k}: {v:.2f}")

"""
task2_change_point.py
Comprehensive Task 2 module for Bayesian Change Point Modeling.
Covers:
- Data loading and preprocessing
- EDA (Price series and log returns)
- Bayesian change point model
- Trace and posterior visualization
- Change point association with key events
- Quantifying impact
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pymc as pm
import arviz as az

sns.set(style="whitegrid")


# -------------------------------
# 1. Load Data
# -------------------------------
def load_price_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date']).sort_values('Date').reset_index(drop=True)
    # Compute log returns
    df['log_return'] = np.log(df['Price']) - np.log(df['Price'].shift(1))
    df = df.dropna().reset_index(drop=True)
    return df

def load_event_data(file_path: str) -> pd.DataFrame:
    events = pd.read_csv(file_path)
    events['Date'] = pd.to_datetime(events['Date'], errors='coerce')
    events = events.dropna(subset=['Date']).reset_index(drop=True)
    return events


# -------------------------------
# 2. EDA Plots
# -------------------------------
def plot_prices(df: pd.DataFrame, save_path=None):
    plt.figure(figsize=(14, 6))
    plt.plot(df['Date'], df['Price'])
    plt.title("Brent Oil Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()


def plot_log_returns(df: pd.DataFrame, save_path=None):
    plt.figure(figsize=(14, 6))
    plt.plot(df['Date'], df['log_return'])
    plt.title("Brent Oil Log Returns")
    plt.xlabel("Date")
    plt.ylabel("Log Return")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()


# -------------------------------
# 3. Bayesian Change Point Model
# -------------------------------
def build_change_point_model(log_returns: np.ndarray,
                             draws=2000,
                             tune=1000,
                             random_seed=42):

    n = len(log_returns)
    with pm.Model() as model:

        # 1. Change point prior
        tau = pm.DiscreteUniform("tau", lower=0, upper=n - 1)

        # 2. Before/after means
        mu1 = pm.Normal("mu1", mu=0, sigma=0.02)
        mu2 = pm.Normal("mu2", mu=0, sigma=0.02)

        # 3. Shared volatility
        sigma = pm.HalfNormal("sigma", sigma=0.01)

        # 4. Switch function
        idx = np.arange(n)
        mu = pm.math.switch(idx < tau, mu1, mu2)

        # 5. Likelihood
        obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=log_returns)

        # 6. Sampling
        trace = pm.sample(draws=draws,
                          tune=tune,
                          target_accept=0.95,
                          random_seed=random_seed,
                          return_inferencedata=True)
    return model, trace


# -------------------------------
# 4. Trace and Posterior Summaries
# -------------------------------
def run_change_point_model(log_returns):
    import pymc as pm
    import numpy as np

    n = len(log_returns)
    with pm.Model() as model:
        tau = pm.DiscreteUniform("tau", lower=0, upper=n-1)
        mu1 = pm.Normal("mu1", mu=0, sigma=0.02)
        mu2 = pm.Normal("mu2", mu=0, sigma=0.02)
        sigma = pm.HalfNormal("sigma", sigma=0.01)
        idx = np.arange(n)
        mu = pm.math.switch(idx < tau, mu1, mu2)
        obs = pm.Normal("obs", mu=mu, sigma=sigma, observed=log_returns)
        trace = pm.sample(draws=500, tune=500, random_seed=42, return_inferencedata=True)
    return trace

def plot_trace(trace, save_path=None):
    """
    Trace and posterior plots.
    """
    az.plot_trace(trace)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()


def plot_tau_posterior(trace, save_path=None):
    tau_samples = trace.posterior['tau'].values.flatten()
    plt.figure(figsize=(12, 5))
    sns.histplot(tau_samples, bins=50, kde=True)
    plt.title("Posterior Distribution of Change Point (tau)")
    plt.xlabel("Time Index")
    plt.ylabel("Density")
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()


def plot_mu_posteriors(trace, save_path=None):
    mu1_samples = trace.posterior['mu1'].values.flatten()
    mu2_samples = trace.posterior['mu2'].values.flatten()
    plt.figure(figsize=(10, 5))
    sns.kdeplot(mu1_samples, label="mu1 (Before)", shade=True)
    sns.kdeplot(mu2_samples, label="mu2 (After)", shade=True)
    plt.title("Posterior Distributions of mu1 and mu2")
    plt.xlabel("Log Return")
    plt.ylabel("Density")
    plt.legend()
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()


# -------------------------------
# 5. Associate Change Point with Events
# -------------------------------
def associate_change_point_with_events(trace, df, events):
    tau_samples = trace.posterior['tau'].values.flatten()
    tau_median_index = int(np.median(tau_samples))
    change_date = df.loc[tau_median_index, 'Date']

    events_copy = events.copy()
    events_copy['diff_days'] = (events_copy['Date'] - change_date).abs()
    nearest_event = events_copy.loc[events_copy['diff_days'].idxmin()]

    return change_date, nearest_event


# -------------------------------
# 6. Quantify Impact
# -------------------------------
def quantify_impact(trace):
    mu1_samples = trace.posterior['mu1'].values.flatten()
    mu2_samples = trace.posterior['mu2'].values.flatten()

    mu1_mean = np.mean(mu1_samples)
    mu2_mean = np.mean(mu2_samples)
    pct_change = ((mu2_mean - mu1_mean) / abs(mu1_mean) * 100) if abs(mu1_mean) > 1e-8 else np.nan

    return mu1_mean, mu2_mean, pct_change

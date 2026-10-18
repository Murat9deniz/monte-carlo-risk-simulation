# Stochastic Monte Carlo Risk & Profitability Simulation

An applied quantitative research project evaluating business profitability under market uncertainty using Monte Carlo simulation techniques.

## 📌 Project Overview
Industrial and commercial business decisions often rely on static financial forecasts that ignore stochastic risk variables. This project builds a **500-trial Monte Carlo simulation framework** in Python to quantify how variance in customer demand and fluctuating supply costs impact net profitability and downside financial risk.

## 🔬 Methodology & Key Features
- **Stochastic Demand & Cost Generation:** Models variable market demand ($N(\mu, \sigma)$) and production costs using Gaussian distributions.
- **Risk Metrics:** Computes 5th Percentile **Value-at-Risk (VaR)**, standard deviation of earnings, and empirical Probability of Loss.
- **Automated Statistical Reporting:** Generates key summary statistics and probability density plots for quantitative evaluation.

## 🛠 Tech Stack
- **Language:** Python 3.10+
- **Data & Numerical Analysis:** `numpy`, `pandas`, `scipy`
- **Visualization:** `matplotlib`, `seaborn`

## 📊 Sample Output & Statistical Summary
Running `python src/simulation_engine.py` yields the following baseline risk analysis over 500 trials:
- **Mean Expected Profit:** €109,240.50
- **Standard Deviation:** €82,150.12
- **5th Percentile (VaR 95%):** -€22,410.80
- **Downside Risk (Probability of Loss):** 8.40%

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/monte-carlo-risk-simulation.git](https://github.com/YOUR_USERNAME/monte-carlo-risk-simulation.git)
   cd monte-carlo-risk-simulation

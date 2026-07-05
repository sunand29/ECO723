# Brazil Inflation Forecasting (ECO723)

## Overview
This repository contains a data science replication project that forecasts the monthly percentage change of the Brazilian IPCA inflation rate. The primary objective of this project is to systematically compare traditional econometric models against advanced machine learning algorithms to determine the most effective approach for macroeconomic forecasting in an emerging market.

## Methodology
- **Data:** 818 distinct macroeconomic variables spanning from January 2004 to December 2018.
- **Preprocessing:** Missing data was handled via forward filling, variables were transformed to ensure stationarity (first differencing), and features were normalized using standard scaling. Raw IPCA values were strictly removed from the feature set to prevent data leakage.
- **Validation Strategy:** An expanding window forecasting architecture was implemented, utilizing an initial 12-month training block and predicting exactly one month ahead ($h=1$) to rigorously simulate real-world, out-of-sample forecasting.
- **Statistical Testing:** The Diebold-Mariano (DM) test was used to determine if the predictive accuracy of the advanced models was statistically significantly better than a baseline Random Walk.

## Models Evaluated
The project evaluates a suite of models across three distinct categories:
1. **Traditional Baselines:** Random Walk, ARMA(1,1), Data-Rich Phillips Curve.
2. **Factor Models:** Factor-Augmented Vector Autoregression (FAVAR) utilizing Principal Component Analysis (PCA) to extract 3 macroeconomic factors.
3. **Machine Learning:** LASSO Regression, Ridge Regression, Elastic Net, and Random Forest Regressor (100 trees).

## Key Results
Non-linear machine learning algorithms significantly outperformed traditional economic models for inflation forecasting.

*   **Best Model:** Random Forest Regressor
*   **RMSE:** 0.1678
*   **R-Squared:** 0.6408
*   **Statistical Significance:** The Diebold-Mariano test yielded a $p < 0.001$, confirming that the Random Forest model's predictions were statistically significantly better than the Random Walk baseline.

## Repository Contents
*   `brazil-inflation-forecasting_clean.ipynb`: The primary Jupyter Notebook containing the data pipeline, model training, evaluation metrics, and visualizations.
*   `cleaned_data.csv`: The preprocessed dataset containing the 818 macroeconomic variables and the target IPCA index.
*   `clean_data.py`: A utility script used in the early stages of data preparation.

## How to Run
1. Ensure you have Python 3 installed along with `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `scipy`, and `statsmodels`.
2. Open `brazil-inflation-forecasting_clean.ipynb` in Jupyter Notebook or Kaggle.
3. Run the cells sequentially to reproduce the data pipeline, model training, and the final leaderboard generation.

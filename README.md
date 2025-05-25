# Stock-Portfolio-Analysis


# 📈 Stock Price Prediction Tool

A Python-based command-line application that lets users fetch, store, and analyze historical stock data — and forecast the next day's closing price using a regression model. Designed for finance enthusiasts, data scientists, and aspiring quants who want to explore short-term equity price prediction.

---

## 🚀 Features

- ✅ Fetch historical stock prices from Yahoo Finance (`yfinance`)
- ✅ Store and manage data in a local `SQLite` database
- ✅ Input stock tickers manually via CLI
- ✅ Clear and reset the database on demand
- ✅ Train a regression model to forecast next-day closing prices
- ✅ Evaluate model accuracy using MAE and RMSE
- ✅ Modular codebase: easy to extend and adapt

---

## 🧠 Machine Learning Approach

- **Model**: Linear Regression (via `scikit-learn`)
- **Features**: Previous N closing prices (time-series lag features)
- **Target**: Next-day closing price
- **Metrics**: Mean Absolute Error (MAE), Root Mean Squared Error (RMSE)

---

## 🗂 Project Structure

stock-predictor/
│
├── main.py # CLI interface for users
├── populate_db.py # Fetches and stores stock data
├── manage_db.py # Handles database table creation and clearing
├── train_model.py # Trains and evaluates ML model
├── portfolio.db # SQLite database (auto-generated)
├── requirements.txt # Dependencies
└── README.md # Project documentation

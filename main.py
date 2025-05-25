from populate_db import fetch_and_store_data
from train_regression import train_and_predict
from manage_db import clear_prices

def main():
    print("\n📊 Welcome to Stock Predictor \n")

    # Give the user the option to clear previous data
    wipe = input("Do you want to clear existing stock data? (yes/no): ").strip().lower()
    if wipe == "yes":
        clear_prices()
    
    # Get tickers
    tickers = input("Enter comma-separated stock tickers (e.g., AAPL,MSFT,GOOGL): ")
    tickers = [t.strip().upper() for t in tickers.split(",")]

    # Download and store data
    fetch_and_store_data(tickers)

    # Train model and predict
    for ticker in tickers:
        train_and_predict(ticker)

if __name__ == "__main__":
    main()

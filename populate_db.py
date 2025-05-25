import sqlite3
import yfinance as yf
from datetime import datetime,timedelta

def fetch_and_store_data(tickers):
    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            ticker TEXT,
            date TEXT,
            close REAL
        )
    """)

    for ticker in tickers:
        print(f"⬇️ Fetching {ticker}...")
        df = yf.download(ticker, period="6mo")[['Close']].reset_index()
        df.columns = ['date', 'close']
        df['ticker'] = ticker

        # Insert to DB
        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO prices (ticker, date, close)
                VALUES (?, ?, ?)
            """, (ticker, row['date'].strftime("%Y-%m-%d"), row['close']))

    conn.commit()
    conn.close()
    print("✅ Data stored in database.")

import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, root_mean_squared_error
from sklearn.model_selection import train_test_split

def train_and_predict(ticker, window_size=5):
    conn = sqlite3.connect("portfolio.db")
    df = pd.read_sql("""
        SELECT date, close FROM prices
        WHERE ticker = ?
        ORDER BY date ASC
    """, conn, params=(ticker,))
    conn.close()

    if len(df) < window_size + 1:
        print(f"❌ Not enough data for {ticker}")
        return

    df.reset_index(drop=True, inplace=True)
    X, y = [], []

    for i in range(len(df) - window_size):
        X.append(df['close'].iloc[i:i+window_size].values)
        y.append(df['close'].iloc[i+window_size])

    X = pd.DataFrame(X)
    y = pd.Series(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = root_mean_squared_error(y_test, y_pred)

    print(f"\n📈 {ticker} — MAE: ${mae:.2f}, RMSE: ${rmse:.2f}")
    latest_window = df['close'].iloc[-window_size:].values.reshape(1, -1)
    next_day = model.predict(latest_window)[0]
    print(f"🔮 Predicted next close: ${next_day:.2f}")
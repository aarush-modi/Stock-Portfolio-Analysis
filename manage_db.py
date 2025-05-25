import sqlite3

def clear_prices():
    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM prices")
    conn.commit()
    conn.close()
    print("🗑️ All data deleted from prices table.")
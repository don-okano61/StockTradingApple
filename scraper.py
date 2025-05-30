import yfinance as yf

# Beispiel: Apple (AAPL)
TICKER = "AAPL"

def scrape_stock_prices():
    stock = yf.Ticker(TICKER)
    history = stock.history(period="1mo")  # Letzte Monatspreise abrufen

    dates = history.index.strftime("%Y-%m-%d").tolist()  # Datumsformat anpassen
    prices = history["Close"].tolist()  # Schlusskurse abrufen

    return dates, prices

# Testen, ob die Funktion funktioniert
if __name__ == "__main__":
    dates, prices = scrape_stock_prices()
    print("Gescrapte Daten:")
    for date, price in zip(dates[:5], prices[:5]):  # Zeigt die ersten 5 Daten
        print(f"{date}: {price}")
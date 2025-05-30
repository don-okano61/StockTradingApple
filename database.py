import psycopg2
from scraper import scrape_stock_prices
import os

# Umgebungsvariable für UTF-8 setzen (nur nötig auf Windows)
os.environ["PYTHONUTF8"] = "1"

# Verbindung zur PostgreSQL-Datenbank herstellen
conn = psycopg2.connect(
    dbname="finance_db",
    user="postgres",
    password="",            #Type here your personal password
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# PostgreSQL-Client-Encoding explizit setzen
cursor.execute("SET client_encoding TO 'UTF8'")

# Tabelle erstellen
cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_prices (
        date VARCHAR(20),
        price FLOAT
    )
""")
conn.commit()

# Daten abrufen
dates, prices = scrape_stock_prices()

# Encoding-Konvertierung für gescrapte Daten
dates = [date.encode("latin1").decode("utf-8", "ignore") for date in dates]  # Sichere Zeichenumwandlung

# Daten speichern
for date, price in zip(dates, prices):
    print(date)  # Debugging: Prüfen, ob problematische Zeichen enthalten sind
    cursor.execute("INSERT INTO stock_prices (date, price) VALUES (%s, %s)", (date, price))

conn.commit()
cursor.close()
conn.close()
print("Daten erfolgreich gespeichert!")
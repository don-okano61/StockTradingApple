import psycopg2
import matplotlib.pyplot as plt

# Verbindung zur Datenbank
conn = psycopg2.connect(dbname="finance_db", user="postgres", password="yjt65nc5", host="localhost", port="5432")
cursor = conn.cursor()

# Daten abrufen
cursor.execute("SELECT date, price FROM stock_prices")
data = cursor.fetchall()

cursor.close()
conn.close()

# Daten für die Visualisierung vorbereiten
dates = [row[0] for row in data]
prices = [row[1] for row in data]

# Plot erstellen
plt.figure(figsize=(10, 5))
plt.plot(dates, prices, marker='o', linestyle='-')
plt.xlabel("Datum")
plt.ylabel("Preis in USD")
plt.title("Aktienkurs von Apple")
plt.xticks(rotation=45)
plt.show()
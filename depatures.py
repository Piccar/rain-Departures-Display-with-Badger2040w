import urequests as requests
import badger2040
from time import sleep
from machine import Pin

# --- URL zur JSON-API ---
API_URL = "https://dbf.finalrewind.org/station.json"

# --- Initialisierung des Displays ---
badger = badger2040.Badger2040()
badger.set_update_speed(badger2040.UPDATE_TURBO)
badger.connect()

# --- Funktion zur API-Anfrage ---
def fetch_departures():
    try:
        response = requests.get(API_URL)
        print(f"API Response Status: {response.status_code}")  # Debugging-Ausgabe
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Fehler bei der Anfrage. Statuscode: {response.status_code}")
            return None
    except Exception as e:
        print("Fehler beim Abrufen der API:", e)
        return None

# --- Funktion zur Verarbeitung der JSON-Daten ---
def parse_departures(data):
    departures = data.get("departures", [])[:2]
    formatted_departures = []

    for dep in departures:
        planned_time = dep.get("scheduledDeparture", "Unknown")
        delay = dep.get("delayDeparture", 0)
        platform = dep.get("platform", "Unknown")
        destination = dep.get("destination", "Unknown")

        display_time = f"{planned_time} +{delay} Min, Gleis {platform}"
        formatted_departures.append((display_time, destination))

    return formatted_departures

# --- Funktion zur Anzeige auf dem Display ---
def display_departures(departures):
    badger.set_pen(15)  # Weißer Hintergrund
    badger.clear()
    badger.set_pen(0)  # Schwarzer Text
    badger.set_font("bitmap8")
    badger.set_thickness(2)

    if not departures:
        badger.text("No data available", 20, 50, scale=3)
    else:
        y_pos = 10
        for display_time, destination in departures:
            badger.text(display_time, 0, y_pos, scale=3)
            badger.text(destination, 0, y_pos + 25, scale=3)
            y_pos += 60

    badger.update()

# --- Hauptschleife ---
while True:
    print("Fetching Data...")
    data = fetch_departures()
    if data:
        departures = parse_departures(data)
        print(f"Departures: {departures}")
        display_departures(departures)
    else:
        print("No data fetched")

    sleep(300)

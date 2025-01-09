# Train Departures Display with Badger2040

This project fetches train departure information from a public JSON API and displays it on the [Badger2040](https://shop.pimoroni.com/products/badger-2040) e-ink display. The code retrieves the next two train departures from the station and updates the display every five minutes.

## Features

- **Fetches live train departure data** from the JSON API provided by [dbf.finalrewind.org](https://dbf.finalrewind.org).
- **Displays train schedules** including planned departure time, delay (in minutes), platform number, and destination.
- **Automatic updates every 5 minutes** to keep the displayed information up to date.

## Prerequisites

- Badger2040 e-ink display
- MicroPython environment set up on the Badger2040
- Wi-Fi connection for the device

## How It Works

1. The script connects to the API endpoint: `https://dbf.finalrewind.org/station.json`.
2. It retrieves the JSON data and parses the first two train departures.
3. The information is formatted as:

Scheduled Departure Time + Delay in Minutes, Platform Destination

4. The display is updated every five minutes with the latest data.

## Code Structure

### `fetch_departures()`

This function makes a GET request to the API and retrieves the JSON response.

### `parse_departures(data)`

Parses the JSON data to extract the next two train departures, including the planned departure time, delay, platform number, and destination.

### `display_departures(departures)`

Formats and displays the extracted departure information on the Badger2040 e-ink screen.

### Main Loop

The script runs in an infinite loop, fetching data and updating the display every five minutes.

## Example Output

09:19 +3 Min, Gleis 4 Köln-Worringen

09:21 +1 Min, Gleis 3 Ratingen Ost


## How to Use

1. Upload the script to your Badger2040 device.
2. Ensure the device is connected to Wi-Fi.
3. Run the script to start displaying live train departure information.

## API Information

The data is fetched from the following API endpoint:

https://dbf.finalrewind.org/


This endpoint provides real-time departure data for a station.

## Customization

- To use a different station, modify the `API_URL` variable in the script with the desired station's JSON URL.
- Adjust the update interval by changing the `sleep(300)` value in the main loop.

## Dependencies

- `urequests`: For making HTTP requests
- `badger2040`: For interacting with the Badger2040 hardware

## License

This project is licensed under the MIT License. Feel free to use and modify the code as needed.


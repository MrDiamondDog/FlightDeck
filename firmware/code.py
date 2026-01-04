# https://learn.adafruit.com/rgb-led-matrices-matrix-panels-with-circuitpython/
import board
import os
import time
import terminalio
import displayio
import rgbmatrix
import framebufferio
import wifi
import adafruit_requests
import adafruit_connection_manager
import adafruit_display_text.label

# Get WiFi details, ensure these are setup in settings.toml
ssid = os.getenv("CIRCUITPY_WIFI_SSID")
password = os.getenv("CIRCUITPY_WIFI_PASSWORD")

# Initalize Wifi, Socket Pool, Request Session
pool = adafruit_connection_manager.get_radio_socketpool(wifi.radio)
ssl_context = adafruit_connection_manager.get_radio_ssl_context(wifi.radio)
requests = adafruit_requests.Session(pool, ssl_context)
rssi = wifi.radio.ap_info.rssi

print(f"Connecting to {ssid}...")
print(f"Signal Strength: {rssi}")
try:
    # Connect to the Wi-Fi network
    wifi.radio.connect(ssid, password)
except OSError as e:
    print(f"OSError: {e}")
print("Wifi Connected")

print("Initializing display")

displayio.release_displays()
matrix = rgbmatrix.RGBMatrix(
    width=64, bit_depth=4,
    rgb_pins=[
        board.MTX_R1,
        board.MTX_G1,
        board.MTX_B1,
        board.MTX_R2,
        board.MTX_G2,
        board.MTX_B2
    ],
    addr_pins=[
        board.MTX_ADDRA,
        board.MTX_ADDRB,
        board.MTX_ADDRC,
        board.MTX_ADDRD
    ],
    clock_pin=board.MTX_CLK,
    latch_pin=board.MTX_LAT,
    output_enable_pin=board.MTX_OE
)

display = framebufferio.FramebufferDisplay(matrix)

network = matrix.network
graphics = matrix.graphics

g = displayio.Group()

# Uses arlabs.co API
flightsApi = "https://airlabs.co/api/v9/flights"
headers = {"user-agent": "FlightDeck/1.0.0"}

apiKey = os.getenv("AIRLABS_API_KEY")

minLat = min(os.getenv("MIN_LAT"), os.getenv("MAX_LAT"))
minLon = min(os.getenv("MIN_LON"), os.getenv("MAX_LON"))
maxLat = max(os.getenv("MIN_LAT"), os.getenv("MAX_LAT"))
maxLon = max(os.getenv("MIN_LON"), os.getenv("MAX_LON"))

def get_nearby_flights():
    with requests.get(f"{flightsApi}?api_key={apiKey}&bbox={minLat},{minLon},{maxLat},{maxLon}", headers=headers) as response:
        json_data = response.json().response[0]
        data = {
            "altitude": json_data["alt"],
            "speed": json_data["speed"],
            "number": json_data["flight_icao"],
            "aircraft": json_data["aircraft_icao"],
            "fromCode": json_data["dep_iata"],
            "toCode": json_data["arr_iata"],
            "registration": json_data["reg_number"]
        }
    
    return data

def text(text, x, y, color = 0xffffff):
    line = adafruit_display_text.label.Label(
        terminalio.FONT,
        color=color,
        text=text,
    )
    line.x = x
    line.y = y

    g.append(line)

    return line

flightNum = text("", 0, 0)
flightAircraft = text("", 0, 6)
flightRoute = text("", 0, 12)
flightAltitude = text("", 0, 18)
flightRegistration = text("", 0, 24)

display.root_group = g

while True:
    time.sleep(30)

    data = get_nearby_flights()

    if not data:
        flightNum.text = ""
        flightAircraft.text = ""
        flightRoute.text = ""
        flightAltitude.text = ""
        flightRegistration.text = ""
        pass

    flightNum.text = data.number
    flightAircraft.text = data.aircraft
    flightRoute.text = f"{data.fromCode}-{data.toCode}"
    flightAltitude.text = f"{data.altitude}ft"
    flightRegistration.text = data.registration

    pass
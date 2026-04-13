import urequests
import time
import wifi_man
import ble_scanner
import logger

SSID       = "your_wifi_ssid"
PASSWORD   = "your_wifi_password"
SERVER_URL = "http://your-server.com/api/beacons"
DEVICE_ID  = "esp32-01"
INTERVAL_S = 30  # how often to scan + send

def send(payload):
    try:
        headers = {"Content-Type": "application/json"}
        res = urequests.post(SERVER_URL, data=payload, headers=headers)
        print("Server response:", res.status_code, res.text)
        res.close()
    except Exception as e:
        print("Send failed:", e)

wifi_man.connect_wifi()
while True:
    print("Scanning BLE...")
    beacons = ble_scanner.scan(duration_ms=5000)
    print(f"Found {len(beacons)} beacons")

    payload = logger.build_payload(beacons, DEVICE_ID)
    print("Payload:", payload)

    send(payload)
    time.sleep(INTERVAL_S)

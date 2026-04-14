import urequests
import time
import wifi_man
import ble_scanner
import logger

SERVER_URL = "PUT IP HERE"
DEVICE_ID  = "esp32-room_blank"
INTERVAL_S = 30

def build_payload(scan_results, device_id="esp32-01"):
    return json.dumps({ "device_id": device_id, "timestamp": time.time(), "beacon_count": len(scan_results), "beacons": scan_results })


def send(payload):
    try:
        headers = {"Content-Type": "application/json"}
        res = urequests.post(SERVER_URL, data=payload, headers=headers)
        print("response:", res.status_code, res.text)
        res.close()
    except Exception as e:
        print("failed. error:", e)

wifi_man.wificonnect("ss")
while True:
    print("Scanning BLE...")
    beacons = ble_scanner.scan(duration_ms=5000)
    print(f"found {len(beacons)} beacons")

    payload = build_payload(beacons, DEVICE_ID)
    print("payload:", payload)

    send(payload)
    time.sleep(INTERVAL_S)

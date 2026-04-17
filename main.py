import urequests
import time
import wifi_man
import ble_scanner
import json

serv_addr = "http://blah.blah.blah:6666"
Device_id  = "esp32-room_blank"


def build_payload(scan_results, device_id="esp32-01"):
    return json.dumps({ "device_id": device_id,
                        "timestamp": time.time(),
                        "beacon_count": len(scan_results),
                        "beacons": scan_results
                        })


def send(payload):
    try:
        headers = {"Content-Type": "application/json"}
        res = urequests.post(serv_addr, data=payload, headers=headers)
        print("response:", res.status_code, res.text)
        res.close()
    except Exception as e:
        print("failed. error:", e)

wifi_man.wificonnect("workstation","passowrd")

while True:
    print("Scanning BLE...")
    beacons = ble_scanner.scan(duration_ms=5000)
    print(f"found {len(beacons)} beacons")

    payload = build_payload(beacons, Device_id)
    #print("payload:", payload)

    response = send(payload)
    time.sleep(1)
    if response and "AFFIRM" in response:
        print("Affirmed, rescanning...")

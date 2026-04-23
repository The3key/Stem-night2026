    import machine
import time
import wifi_man
import ble_scanner
import json
import socket

Device_id  = "esp32-room_blank"


def build_payload(scan_results, device_id="esp32-01"):
    return json.dumps({ "device_id": device_id,
                        "timestamp": time.time(),
                        "beacon_count": len(scan_results),
                        "beacons": scan_results
                        })


def send(payload):
    try:
        s = socket.socket()
        s.connect((hi, 6666))
        s.send(payload.encode('utf-8'))
        response = s.recv(1048576)
        print("response:", response.decode('utf-8'))
        s.close()
    except Exception as e:
        print("failed. error:", e)

wifi_man.wificonnect("workstation","password")


print("Scanning BLE...")
beacons = ble_scanner.scan(duration_ms=5000)
print(f"found {len(beacons)} beacons")

payload = build_payload(beacons, Device_id)
    

response = send(payload)
time.sleep(10)
machine.reset()
    
        

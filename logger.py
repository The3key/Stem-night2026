import json
import time

def build_payload(scan_results, device_id="esp32-01"):
    return json.dumps({
        "device_id": device_id,
        "timestamp": time.time(),  # seconds since epoch (or boot)
        "beacon_count": len(scan_results),
        "beacons": scan_results
    })

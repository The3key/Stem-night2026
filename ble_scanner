import bluetooth
import time

_IRQ_SCAN_RESULT = 5
_IRQ_SCAN_DONE   = 6

results = []

def _irq(event, data):
    if event == _IRQ_SCAN_RESULT:
        addr_type, addr, adv_type, rssi, adv_data = data
        entry = {
            "mac":  ":".join("{:02X}".format(b) for b in bytes(addr)),
            "rssi": rssi,
            "adv_type": adv_type,
            "raw": bytes(adv_data).hex()
        }
        
        macs = [r["mac"] for r in results]
        if entry["mac"] not in macs:
            results.append(entry)

def scan(duration_ms=5000):
    global results
    results = []
    ble = bluetooth.BLE()
    ble.active(True)
    time.sleep(0.1)
    ble.irq(_irq)
    ble.gap_scan(duration_ms, 30000, 30000)
    time.sleep_ms(duration_ms + 500)
    ble.gap_scan(None)
    
    return results

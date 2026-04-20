import network
import time
import machine

try:
    sys_log = open('SYS_LOG.txt',"a")
except OSError:
    print("UNABLE TO OPEN SYS_LOG; REBOOTING!")
    machine.reset()

def wificonnect(ssid,password):
    wlan = network.WLAN(network.STA_IF)
    
    wlan.active(False)
    time.sleep(1)
    wlan.active(True)
    #reset current network status
    
    attempt = 0
    if not wlan.isconnected():
        print("attempt connect to " +str(ssid))
        wlan.connect(ssid,password)
        
        while not wlan.isconnected():
            print("attempt: " + str(attempt) + str(wlan.status()))
            attempt += 1
            if attempt >= 20:
                print("connection failed! rebooting...")
                sys_log.write("connection failed. code: " + str(wlan.status()))
                sys_log.close()
                machine.reset()
            time.sleep(1)
        
    internetconfig = wlan.ifconfig()
    print('connection successful!', wlan.ifconfig())
    sys_log.write("[" + str(time.localtime()) + "]: " + str(internetconfig[0]))
    sys_log.flush()
    print('current ip: ' + str(internetconfig[0]))
    return internetconfig[0]
    


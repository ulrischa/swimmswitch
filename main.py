from machine import Pin
import time
from phew import server, connect_to_wifi

wifi_ssid= "xxx"
wifi_pw = "xxx"

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

def over_under_check():
    if button.value():
        return "Over Water"
    else:
        return "Under water"

def bootstrap():
    ip = connect_to_wifi(wifi_ssid, wifi_pw)
    if ip is not None:
        print("Get status from: http://"+ip+"/status \n")

        
@server.route("/status", methods=["GET"])
def send_status(request):
    stat = over_under_check()
    return stat, 200


@server.catchall()
def catchall(request):
  return "Not found", 404


bootstrap()
server.run()

import os
from tesla_powerwall import Powerwall

def getenv(var):
    val = os.getenv(var)
    if val is None:
        raise ValueError(f"{var} must be set")
    return val

ip = getenv("POWERWALL_IP")
password = getenv("POWERWALL_PASSWORD")

power_wall = Powerwall(ip)
power_wall.login(password)

# Identify the powerwall version
power_wall.detect_and_pin_version()
print("Detected and pinned version: {}".format(power_wall.get_pinned_version()))

print("Current charge: {}".format(power_wall.get_charge()))
print("Device Type: {}".format(power_wall.get_device_type()))
print("Site Name: {}".format(power_wall.get_site_info().site_name))
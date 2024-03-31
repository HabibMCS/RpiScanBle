#!/usr/bin/env python
import bluetooth

def scan_devices():
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, >
    return nearby_devices

def main():
    print("Scanning for nearby Bluetooth devices...")
    devices = scan_devices()
    print("Found {} devices:".format(len(devices)))
    for addr, name in devices:
        print("  - MAC Address: {}, Name: {}".format(addr, name))

if __name__ == "__main__":
    main()
# See
# - https://github.com/pybluez/pybluez/tree/0.23/examples/ble
# - https://pypi.org/project/gattlib/

# GATT Hearing Aid Profile
#
# Services:
#   -
#
# All BLE characteristic UUIDs are of the form:
#    0000XXXX-0000-1000-8000-00805f9b34fb
# So `2a00` is `00002a00-0000-1000-8000-00805f9b34fb`

import time
import sys

import bluetooth.ble as ble

from blutooth.uuid_database import UuidDatabase

# import pdb; pdb.set_trace()

print("Scanning for BLE devices... (indefinately)")

service = ble.DiscoveryService()  # DiscoveryService("hci0")

time_taken = 0
timeout = 5
devices = []
while len(devices) == 0:
    try:
        devices = service.discover(timeout)
    except RuntimeError as e:
        sys.exit(f"ERROR: {e}")

    time_taken += timeout
    print(f"...found {len(devices)} device(s) ({time_taken} seconds)")

print("\n=== Devices ===")
for address, name in devices.items():
    print(f"name: {name}, address: {address}")

# required! `devices` likely points to the same GattLib C-object, which is
# causing some mayham, leading to segmentation faults
addresses = devices.copy()

for address, name in addresses.items():
    req = ble.GATTRequester(address)

    print(f"\n==> [device]: {address} ({name}) ===")
    req.read_by_uuid('2a24') # We get a segmentation fault if we don't do this ?

    print(f"\nServices:")
    for serv in req.discover_primary():
        name = UuidDatabase().uuid(serv['uuid'])['name']
        print(f"name: {name}, uuid: {serv['uuid']}, start: {serv['start']}, end: {serv['end']}")

    print(f"\nCharacteristics:")
    for char in req.discover_characteristics():
        name = UuidDatabase().uuid(char['uuid'])['name']
        print(
            f"name: {name}, uuid: {char['uuid']}, handle: {char['handle']}, value_handle: {char['value_handle']}, properties: {char['properties']}"
        )
    # req.disconnect()

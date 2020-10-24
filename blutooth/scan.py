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

# RuntimeError: Device is not responding!
# RuntimeError: Channel or attrib disconnected

# Bluetooth 128-bit UUIDs
#
#
#     0000xxxx-0000-1000-8000-00805F9B34FB  # 16 bit
#     xxxxxxxx-0000-1000-8000-00805F9B34FB  # 32 bit
#     xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx  # 128 bit custom UUIDs

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
    if name != 'SET-A15': continue  # TODO: rm
    print(f"name: {name}, address: {address}")

for address, name in devices.items():
    if name != 'SET-A15': continue  # TODO: rm
    req = ble.GATTRequester(address)

    print(f"\n==> [device]: {address} ({name}) ===")

    # We get a segmentation fault if we don't do this ?
    req.read_by_uuid('2a24')

    print(f"\nServices:")
    for serv in req.discover_primary():
        db = UuidDatabase()
        name = db.uuid(serv['uuid'])['name']
        value = db.uuid(serv['uuid'])['name']
        uuid = serv['uuid'][4:8]
        print(f"({uuid}) {name}, start: {serv['start']}, end: {serv['end']}")

    print(f"\nCharacteristics:")
    for char in req.discover_characteristics():
        db = UuidDatabase()
        name = db.uuid(char['uuid'])['name']
        name = str.ljust(name, 42)
        value = req.read_by_handle(char['value_handle'])[0]
        properties = {
            2: 'READ',
            34: 'INDICATE, READ',
            18: 'NOTIFY, READ',
            10: 'READ, WRITE'
        }
        properties = properties[char['properties']]
        uuid = char['uuid'][4:8]
        print(
            f"({uuid}) {name}: {value}, handle: {char['handle']}, properties: {properties}"
        )

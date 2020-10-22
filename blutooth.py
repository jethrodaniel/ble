# See
# - https://github.com/pybluez/pybluez/tree/0.23/examples/ble
# - https://pypi.org/project/gattlib/

import time
import sys

import bluetooth.ble as ble

print("Scanning for BLE devices... (indefinately)")

service = ble.DiscoveryService() # DiscoveryService("hci0")

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

# import pdb; pdb.set_trace()

db = {
  'name': '00002a24-0000-1000-8000-00805f9b34fb',
  'bluetooth chip': '00002a29-0000-1000-8000-00805f9b34fb'
}

# required! `devices` likely points to the same GattLib C-object, which is
# causing some mayham, leading to segmentation faults
addresses = devices.copy()

for address, name in addresses.items():
  req = ble.GATTRequester(address)

  print(f"\n==> [device]: {address} ({name}) ===")
  print(f"\nInfo we actually understand:")
  for name, uuid in db.items():
    print(f"{name}: {req.read_by_uuid(uuid)}")

  print(f"\nServices:")
  for serv in req.discover_primary():
    print(f"uuid: {serv['uuid']}, start: {serv['start']}, end: {serv['end']}")

  print(f"\nCharacteristics:")
  for char in req.discover_characteristics():
    val = req.read_by_uuid(char['uuid'])
    print(f"uuid: {char['uuid']}, handle: {char['handle']}, value_handle: {char['value_handle']}, properties: {char['properties']}, value: {val}")
  req.disconnect()
  # req.write_by_handle(0x10, bytes([14, 4, 56]))


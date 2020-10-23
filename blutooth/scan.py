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
import json

import bluetooth.ble as ble

# import pdb; pdb.set_trace()

class UuidDatabase:
  def __init__(self):
    with open('third_party/bluetooth-numbers-database/v1/characteristic_uuids.json') as f:
      self.data = json.load(f)

  def sanitize_uuid(self, uuid_value):
    """Convert `00001800-0000-1000-8000-00805f9b34fb` to `1800`"""
    return uuid_value[4:8]

  def uuid(self, uuid_value):
    res = list(filter(lambda row: row['uuid'] == str.upper(uuid_value[4:8]), self.data))
    if len(res) > 0: return res[0]
    else:            return ''

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

# required! `devices` likely points to the same GattLib C-object, which is
# causing some mayham, leading to segmentation faults
addresses = devices.copy()

db = {
  'name': '00002a24-0000-1000-8000-00805f9b34fb',
  'bluetooth chip': '00002a29-0000-1000-8000-00805f9b34fb'
}

for address, name in addresses.items():
  req = ble.GATTRequester(address)

  print(f"\n==> [device]: {address} ({name}) ===")
  print(f"\nInfo we actually understand:")
  for name, uuid in db.items():
    print(f"{name}: {req.read_by_uuid(uuid)}")
    print(f"service type: {req.read_by_handle(0x001)}") # Generic Attribute
    print(f"service type: {req.read_by_handle(0x005)}") # Generic Access


  # Service values: https://www.bluetooth.com/specifications/assigned-numbers/
  #
  # | GATT Service | 0x1800 | Generic Access
  print(f"\nServices:")
  for serv in req.discover_primary():
    print(f"uuid: {serv['uuid']}, start: {serv['start']}, end: {serv['end']}")
    # import pdb; pdb.set_trace()
    # name = UuidDatabase().uuid(serv['uuid'])
    # print(f"name: {name}, uuid: {serv['uuid']}, start: {serv['start']}, end: {serv['end']}")

  # Characteristic values: https://www.bluetooth.com/specifications/assigned-numbers/
  #
  # | GATT Characteristic and Object Type | 0x2A00 | Device Name
  print(f"\nCharacteristics:")
  for char in req.discover_characteristics():
    name = UuidDatabase().uuid(serv['uuid'])
    print(f"name: {name}, uuid: {char['uuid']}, handle: {char['handle']}, value_handle: {char['value_handle']}, properties: {char['properties']}")
  req.disconnect()


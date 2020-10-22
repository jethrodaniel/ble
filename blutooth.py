import time
import sys

# https://github.com/pybluez/pybluez/tree/0.23/examples/ble
from bluetooth.ble import DiscoveryService, GATTRequester
# import bluetooth.ble as ble

# https://pypi.org/project/gattlib/


# Generic Attribute Profile (GATT)
# +---------------------+--------+----------------------------------+
# | Name                | Value  | Purpose                          |
# +---------------------+--------+----------------------------------+
# | Service Declaration | 0x2800 | what kind of service (see table) |
# +---------------------+--------+----------------------------------+
# | | 0x2800 |
# +---------------------+--------+----------------------------------+


print("Scanning for BLE devices... (indefinately)")

service = DiscoveryService() # DiscoveryService("hci0")

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

import pdb; pdb.set_trace()
for address, name in devices.items()[0]:
  print(f"\n==> {address} ({name})")
  req = GATTRequester(address)

  print(f"Services:")
  # for serv in req.discover_primary():
  #   print(f"uuid: {serv['uuid']}, start: {serv['start']}, end: {serv['end']}")

  print(f"Characteristics:")
  for char in req.discover_characteristics():
    val = true # req.read_by_uuid(char['uuid'])
    # time.sleep(5)
    print(f"uuid: {char['uuid']}, handle: {char['handle']}, value_handle: {char['value_handle']}, properties: {char['properties']}, value: {val}")
    # print(f"uuid: {char['uuid']}, handle: {char['handle']}, value_handle: {char['value_handle']}, properties: {char['properties']}")

  # req.write_by_handle(0x10, bytes([14, 4, 56]))


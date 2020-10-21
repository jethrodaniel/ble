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

timeout = 5
devices = []
while len(devices) == 0:
  devices = service.discover(timeout)
  print(f"found {len(devices)} devices ({timeout} seconds)")

for address, name in devices.items():
  print(f"name: {name}, address: {address}")

# import pdb; pdb.set_trace()

req = GATTRequester(list(devices.items())[0][0]) # first address
name = req.read_by_uuid("00002a00-0000-1000-8000-00805f9b34fb")[0]
# steps = req.read_by_handle(0x18)[0]

print(f"Services:")
for serv in req.discover_primary():
  print(f"uuid: {serv['uuid']}, start: {serv['start']}, end: {serv['end']}")
  # for i in req.read_by_uuid(serv['uuid']):
    # print(f"--\n{i}")

print(f"Characteristics:")
for char in req.discover_characteristics():
  print(f"uuid: {char['uuid']}, handle: {char['handle']}, value_handle: {char['value_handle']}, properties: {char['properties']}")
# req.write_by_handle(0x10, bytes([14, 4, 56]))


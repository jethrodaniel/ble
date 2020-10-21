# https://github.com/pybluez/pybluez/tree/0.23/examples/ble
from bluetooth.ble import DiscoveryService, GATTRequester
# import bluetooth.ble as ble

# https://pypi.org/project/gattlib/

print("Scanning for BLE devices...")

# service = DiscoveryService("hci0")
service = DiscoveryService()
devices = service.discover(10)

for address, name in devices.items():
  print(f"name: {name}, address: {address}")

# import pdb; pdb.set_trace()

req = GATTRequester(list(devices.items())[0][0]) # first address
name = req.read_by_uuid("00002a00-0000-1000-8000-00805f9b34fb")[0]
# steps = req.read_by_handle(0x18)[0]

print(f"Services:")
for serv in req.discover_primary():
	print(f"uuid: {serv['uuid']}, start: {serv['start']}, end: {serv['end']}")
for char in req.discover_characteristics():
	print(f"uuid: {char['uuid']}, handle: {char['handle']}, value_handle: {char['value_handle']}, properties: {char['properties']}")



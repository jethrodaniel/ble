import json

class UuidDatabase:
  SUBMODULE = 'third_party/bluetooth-numbers-database'
  def __init__(self):
    json_path = lambda name: f"{self.SUBMODULE}/v1/{name}.json"
    json_file = lambda name:

    with open(json_path('characteristic_uuids')) as f:
      self.data = json.load(f)

  def sanitize_uuid(self, uuid_value):
    """Convert `00001800-0000-1000-8000-00805f9b34fb` to `1800`"""
    return str.upper(uuid_value[4:8])

  def uuid(self, uuid_value):
    res = list(filter(lambda row: row['uuid'] == self.sanitize_uuid(uuid_value), self.data))
    if len(res) > 0: return res[0]
    return ''

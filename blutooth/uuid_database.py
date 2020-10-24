import json


class UuidDatabase:
    '''
    Converts long-form UUIDs to human-readable info
    '''

    SUBMODULE = 'third_party/bluetooth-numbers-database'

    def __init__(self):
        json_path = lambda name: f"{self.SUBMODULE}/v1/{name}.json"

        with open(json_path('characteristic_uuids')) as f:
            self.data = json.load(f)
        with open(json_path('service_uuids')) as f:
            self.data += json.load(f)
        with open(json_path('descriptor_uuids')) as f:
            self.data += json.load(f)

    def sanitize_uuid(self, uuid_value):
        """Convert 128 bit BLE UUIDs into 16/32/128 bit values.

        TODO: for now, we only convert to 16 bit

        The base UUID for 16 bit identififers is

            0000xxxx-0000-1000-8000-00805f9b34fb

        For 32 bit identififers

            xxxxxxxx-0000-1000-8000-00805f9b34fb
        """
        return str.upper(uuid_value[4:8])

    def uuid(self, uuid_value):
        res = list(
            filter(lambda row: row['uuid'] == self.sanitize_uuid(uuid_value),
                   self.data))
        if len(res) > 0: return res[0]
        return {'name': 'Unknown'}

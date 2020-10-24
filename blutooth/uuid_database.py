import json


class InvalidUuid(ValueError):
    pass


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
        u = uuid_value[4:8]
        if not uuid_value == f"0000{u}-0000-1000-8000-00805f9b34fb":
            raise InvalidUuid("UUID is invalid for 16 bit conversion")
        return str.upper(u)

    def __search_for_uuid(self, long_uuid):
        for uuid in self.data:
            try:
                if uuid['uuid'] == self.sanitize_uuid(long_uuid):
                    return uuid
            except InvalidUuid:
                pass
        return None

    def uuid(self, uuid_value):
        res = self.__search_for_uuid(uuid_value)
        if res is not None: return res
        return {'name': 'Unknown'}

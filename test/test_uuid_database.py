import unittest

from blutooth.uuid_database import UuidDatabase


class TestUuidDatabase(unittest.TestCase):
    def setUp(self):
        self.db = UuidDatabase()

    def test_uuid_characteristic(self):
        expected = {
            "name": "Device Name",
            "identifier": "org.bluetooth.characteristic.gap.device_name",
            "uuid": "2A00",
            "source": "gss"
        }
        uuid = '00002a00-0000-1000-8000-00805f9b34fb'
        self.assertEqual(expected, self.db.uuid(uuid))

    def test_uuid_service(self):
        expected = {
            "name": "Generic Access",
            "identifier": "org.bluetooth.service.generic_access",
            "uuid": "1800",
            "source": "gss"
        }
        uuid = '00001800-0000-1000-8000-00805f9b34fb'
        self.assertEqual(expected, self.db.uuid(uuid))

    def test_uuid_invalid_input(self):
        uuid = 'Be Excellent to each other!'
        self.assertEqual({'name': 'Unknown'}, self.db.uuid(uuid))
        # with self.assertRaises(TypeError):
        #   self.db.uuid(uuid)

    def test_sanitize_uuid(self):
        before = '00002a00-0000-1000-8000-00805f9b34fb'
        after = '2A00'
        self.assertEqual(after, self.db.sanitize_uuid(before))

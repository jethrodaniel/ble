import unittest

from blutooth.gatt import Device, Service, Characteristic


class TestDevice(unittest.TestCase):
    def test_device(self):
        d = Device('00:11:22:33:FF:EE', 'Bender')
        self.assertEqual('Bender', d.name)
        self.assertEqual('00:11:22:33:FF:EE', d.address)


class TestService(unittest.TestCase):
    def test_service(self):
        s = Service('2a00', 'Device Name')
        self.assertEqual('2A00', s.uuid)
        self.assertEqual('Device Name', s.name)

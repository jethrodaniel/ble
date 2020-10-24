class Device():
    def __init__(self, address, name=''):
        self.name = name
        self.address = address


class Service():
    def __init__(self, uuid, name=''):
        self.uuid = str.upper(uuid)
        self.name = name


class Characteristic():
    pass

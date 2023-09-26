from brother import Brother

class Family(object):
    name = ""
    head = Brother()
    brothers = []

    def __init__(self, h, b):
        self.name = h.name
        self.head = h
        self.brothers = b
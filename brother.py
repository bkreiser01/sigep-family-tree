class Brother(object):
    name = ""
    role = -1
    big = ""
    littles = []
    ec = ""

    def __init__(self, name, role, big, ec):
        self.name = name
        self.role = role
        self.big = big
        self.ec = ec

    def __repr__(self):
        return f"[{self.name}, {self.role}, {self.big}, {self.ec}]"
    
    def __str__(self):
        return f"[{self.name}, {self.role}, {self.big}, {self.ec}]"
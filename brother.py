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
        return f"{self.name}"
    
    def __str__(self):
        out = f"Name      | {self.name}\nRole      | {self.role}\nBig       | {self.big}\n"
        out += f"Little(s) |"
        if len(self.littles) > 0:
            for i in range(0, len(self.littles)):
                if i == 0:
                    out += f" {self.littles[i].name}"
                else:
                    out += f"\n          | {self.littles[i].name}"
        return out
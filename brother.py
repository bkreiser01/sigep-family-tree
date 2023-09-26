class Brother(object):
    name = ""
    role = -1
    big = ""
    littles = []
    ec = ""

    def find_descendants(self):
        if len(self.littles) == 0:
            return []
        else:
            descendants = []
            for little in self.littles:
                descendants += [little]
                descendants += little.find_descendants()
            return descendants

    def __init__(self, n=None, r=None, b=None, ec=None):
        self.name = n
        self.role = r
        self.big = b
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
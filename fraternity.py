from brother import Brother
import csv

class Fraternity(object):
    name = ""
    brothers = []

    def find_littles(big, bros):
        littles = []
        for bro in bros:
            if bro.big == big.name:
                littles.append(bro)
        big.littles = littles
        return littles

    def __init__(self, data):
        arr = []
        bros = []
        self.name = data.split(".")[0]

        # Parse the CSV
        with open(data, mode ='r') as file:
            csv_reader = csv.reader(file) 

            # displaying the contents of the CSV file
            for line in csv_reader:
                arr += [line]
        
        for elem in arr[1:]:
            self.brothers.append(Brother(elem[0], elem[1], elem[2], elem[3]))
        
        for bro in self.brothers:
            bro.find
    
    def __str__(self):
        arr = []
        out_str = ""
        for bro in self.brothers:
            arr.append(bro.name)
        arr.sort()

        for e in arr:
            out_str += e + '\n'
        return out_str
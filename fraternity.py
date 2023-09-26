from brother import Brother
from family import Family
import csv

class Fraternity(object):
    name = ""
    brothers = []
    founders = []
    families = []

    def __find_littles(self, big):
        littles = []

        # Search through all the brothers
        for bro in self.brothers:

            # If the current brother has big listed as their big.
            # Add the current brother to the little list
            if bro.big == big.name:
                littles.append(bro)

        # Add the found littles to the big's little list
        big.littles = littles

    def __init__(self, data):
        data_arr = []

        # The name of the CSV is the name of the fraternity
        self.name = data.split(".")[0]

        # Parse the CSV, adding all data into an array
        with open(data, mode ='r') as file:
            csv_reader = csv.reader(file) 
            for line in csv_reader:
                data_arr += [line]
        
        # Take all brothers from csv and add them to the brothers list
        for elem in data_arr[1:]:
            self.brothers.append(Brother(elem[0], elem[1], elem[2], elem[3]))
        
        # Find the littles for each brother, if there are any
        # Also determine founders
        founders = []
        for bro in self.brothers:
            self.__find_littles(bro)
            if bro.big == "":
                founders.append(bro)
        
        # Find descendants of each founder
        for founder in founders:
            self.families.append(Family(founder, founder.find_descendants()))
        
        

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        arr = []
        out = ""

        # Sort for readability
        for bro in self.brothers:
            arr.append(bro.name)
        arr.sort()

        for e in arr:
            out += e + '\n'
        out = out[:-1]
        return out
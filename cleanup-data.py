##################################################
## This was created to convert from the old data format to the new one.
## The old one was bad :(
##################################################
import graphviz
import csv
import os

DATA_CSV = 'data.csv'
brother_dict, brother_list, founding_bros, family_colors = {},[],[],[]


# generate brother dictonary
with open(DATA_CSV, mode ='r')as file:
    # reading the CSV file
    csvFile = csv.reader(file) 
    index = 0
    # displaying the contents of the CSV file
    for line in csvFile:
        if index == 0: # read first line which contains founders data
            line[0] = line[0][1:] # gets rid of char \ufeff
            founding_bros = line
        elif index == 1: # read second line which contains family colors
            family_colors = line
            index = 0
            for color in family_colors:
                family_colors[index] = color.replace(" ", "")
                index+=1
            index = 1
        else:
            if line != [] and line[0][0] != '#':
            # checks for dupes
                if line[0] in brother_dict:
                    brother_dict[line[0]] = brother_dict[line[0]] + [line[1]]
                else:
                    brother_dict[line[0]] = [line[1]]
                brother_list += [line[0], line[1]]
        index += 1

# remove dupes from bro list
tmp_list = []
for bro in brother_list:
    if bro not in tmp_list:
        tmp_list += [bro]
brother_list = tmp_list


new_list = {}

with open('clean-data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',)
    writer.writerow(["Name","Role Number","Big","EC Position(s)"])
    for bro in brother_list:
        first_split = bro.split("\\r")
        print(first_split)
        second_split = first_split[1].split(" ")

        bro_name = first_split[0]
        bro_role = second_split[0]
        bro_big = ""
        bro_ec = ""

        if len(second_split) > 1:
            bro_ec += " ".join(second_split[1:])

        for big in brother_dict:
            big_name = big.split("\\r")[0]
            if bro in brother_dict[big]:
                bro_big = big_name
        # print(f"{bro_name},{bro_role},{bro_big},{bro_ec}")
        writer.writerow([bro_name,bro_role,bro_big,bro_ec])

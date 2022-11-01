##################################################
## Author: Brandon Kreiser -1250
## Description: This program generates multiple
##              family trees from a given CSV
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


# creates the main graph
graph_main = graphviz.Digraph(
    engine='dot',
    node_attr={"shape": "box"},
    edge_attr={"arrowhead": "none"}
)

# creates the first subgraph
subgraphs = []
current_subgraph = graphviz.Digraph(
        node_attr={"style": "filled","fillcolor": family_colors[0]}
)

# create a subgraph for each family and nodes for each bro
index = 1
for bro in brother_list:
    if bro in founding_bros:
        subgraphs.append(current_subgraph)
        current_subgraph = graphviz.Digraph(
            node_attr={"style": "filled","fillcolor": family_colors[index]}
        )
        index+=1
    current_subgraph.node(bro, bro)

# iterate through big-little pairs and connect them in their subgraphs
index = 0
for big in brother_dict:
    if big in founding_bros:
        current_subgraph = subgraphs[index]
        index+=1
    for little in brother_dict[big]:
        current_subgraph.edge(big, little)

# join all subgraphs together
for subgraph in subgraphs:
    graph_main.subgraph(subgraph)

graph_main.render('brothers', view=True)
os.remove(os.path.dirname(os.path.abspath(__file__)) + '/brothers')
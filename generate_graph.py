##################################################
## Author: Brandon Kreiser -1250
## Description: This program generates multiple
##              family trees from a given CSV
##################################################
import graphviz
import os

from fraternity import Fraternity

DATA_CSV = 'SigEp.csv'
family_colors = []
  

def find_founders(bros):
    founders = []
    for bro in bros:
        if bro.big == "":
            founders.append(bro)
    return founders

def gen_graph(brother_dict, brother_list, founding_bros):
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


def main():
    fraternity = Fraternity(DATA_CSV)
    
    print(fraternity)

main()
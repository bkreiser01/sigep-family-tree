##################################################
## Author: Brandon Kreiser -1250
## Description: This program generates multiple
##              family trees from a given CSV
##################################################
import graphviz
import os

from fraternity import Fraternity
from brother import Brother

DATA_CSV = 'SigEp.csv'
family_colors = []

def gen_graph(fraternity):
    # creates the main graph
    fraternity_tree = graphviz.Digraph(
        engine='dot',
        node_attr={"shape": "box"},
        edge_attr={"arrowhead": "none"}
    )

    for family in fraternity.families:
        tree = graphviz.Digraph(
            node_attr={"style": "filled","fillcolor": 'Grey'}
        )

        # Add the family head and their littles to the tree
        tree.node(family.head.name, family.head.name)
        for little in family.head.littles:
            tree.edge(family.head.name, little.name)

        # Add the rest of the family to the tree
        for bro in family.brothers:
            tree.node(bro.name, bro.name)
            for little in bro.littles:
                tree.edge(bro.name, little.name)
        
        fraternity_tree.subgraph(tree)
    
    fraternity_tree.render('brothers', view=True)
    os.remove(os.path.dirname(os.path.abspath(__file__)) + '/brothers')
    
    # ===========LEGACY CODE===========
    # # creates the first subgraph
    # subgraphs = []
    # current_subgraph = graphviz.Digraph(
    #         node_attr={"style": "filled","fillcolor": 'Red'}
    # )

    # # create a subgraph for each family and nodes for each bro
    # index = 1
    # for bro in brother_list:
    #     if bro in founding_bros:
    #         subgraphs.append(current_subgraph)
    #         current_subgraph = graphviz.Digraph(
    #             node_attr={"style": "filled","fillcolor": family_colors[index]}
    #         )
    #         index+=1
    #     current_subgraph.node(bro, bro)

    # # iterate through big-little pairs and connect them in their subgraphs
    # index = 0
    # for big in brother_dict:
    #     if big in founding_bros:
    #         current_subgraph = subgraphs[index]
    #         index+=1
    #     for little in brother_dict[big]:
    #         current_subgraph.edge(big, little)


def main():
    gen_graph(Fraternity(DATA_CSV))

main()
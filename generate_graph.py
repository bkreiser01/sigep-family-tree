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

def main():
    gen_graph(Fraternity(DATA_CSV))

main()
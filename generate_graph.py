##################################################
## Author: Brandon Kreiser -1250
## Description: This program generates multiple
##              family trees from a given CSV
##################################################
import graphviz
import os
import random

from fraternity import Fraternity

DATA_CSV = 'SigEp.csv'
family_colors = []

def __format(bro):
    return f"{bro.name}\n{bro.role} {bro.ec}"

def __complementaryColor(my_hex):
    rgb = (my_hex[0:2], my_hex[2:4], my_hex[4:6])
    comp = ['%02X' % (255 - int(a, 16)) for a in rgb]
    return ''.join(comp)

def gen_graph(fraternity):
    # creates the main graph
    fraternity_tree = graphviz.Digraph(
        engine='dot',
        node_attr={"shape": "box"},
        edge_attr={"arrowhead": "none"}
    )

    for family in fraternity.families:
        hexadecimal = ''.join([random.choice('ABCDEF0123456789') for i in range(6)])

        tree = graphviz.Digraph(
            node_attr={
                "style": "filled",
                "fillcolor": '#' + hexadecimal
                }
        )

        # Add the family head and their littles to the tree
        tree.node(__format(family.head), __format(family.head))
        for little in family.head.littles:
            tree.edge(__format(family.head), __format(little))

        # Add the rest of the family to the tree
        for bro in family.brothers:
            tree.node(__format(bro), __format(bro))
            for little in bro.littles:
                tree.edge(__format(bro), __format(little))
        
        fraternity_tree.subgraph(tree)
    
    fraternity_tree.render('brothers', view=True)
    os.remove(os.path.dirname(os.path.abspath(__file__)) + '/brothers')

def main():
    gen_graph(Fraternity(DATA_CSV))

main()
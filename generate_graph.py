##################################################
## Author: Brandon Kreiser -1250
## Description: This program generates multiple
##              family trees from a given CSV
##################################################
import graphviz
import os
import random
import sys

from fraternity import Fraternity

DATA_CSV = 'SigEp.csv'
family_colors = []

def __format(bro):
    return f"{bro.name}\n{bro.role} {bro.ec}"

def generate_random_color(mix=None):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    # Mix the color
    if mix is not None:
        red = (red + mix[0]) // 2
        green = (green + mix[1]) // 2
        blue = (blue + mix[2]) // 2

    return "#{:02x}{:02x}{:02x}".format(red, green, blue)

def gen_graph(fraternity):
    # creates the main graph
    fraternity_tree = graphviz.Digraph(
        engine='dot',
        node_attr={"shape": "box"},
        edge_attr={"arrowhead": "none"}
    )

    for family in fraternity.families:
        # Define tree style
        tree = graphviz.Digraph(
            node_attr={
                "style": "filled",
                "fillcolor": generate_random_color((255,255,255))
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
    gen_graph(Fraternity(sys.argv[1]))

main()
# sigep-family-tree
This is a script to generate a family tree for the New Jersey Alpha chaper of Sigma Phi Epsillon. You may adopt this script to suit your own chapter as well.

## Requirements
* Python
* graphviz version 0.20.1

## Setup
Clone the git repository

Configure `data.csv ` to however you would like (Feel free to use the provided data as a guide)

## How is the `data.csv` formatted
There are three sections to `data.csv`

* List of chapter founders
* List of founders colors
* All big-little relationships

The chapter founders should just be a list of the founders in the format you have decided. For what I believe to be the best look I would follow the below format.

```
First Last\rRole_Num (EC_POSITIONS)
```
An example would look like `Brandon Kreiser\r1250 (VPF)` which just formats the cell nicely

The chaper founders colors is the next line and should just be a list of colors such as. `Color1,Color2,Color3` The script wil ignore any spaces you put in here, so you can allign colors with their founders like so.

```
Ryan Price\r877 (PRES),Pitor Czerchowski\r840
gold                  ,green
```

And last but not least the little pairs should be formatted as such

```
B_First B_Last\rRole_Num (EC_POS),L_First L_Last\rRole_Num (EC_POS)
```

In practice it would looks like this `Luke Langner\r1195 (VPMD),Brandon Kreiser\r1250 (VPF)`

# Running `run.py`
You can run the program by typing `python3 run.py` into the cli. You will get a pdf output named `brothers.pdf`

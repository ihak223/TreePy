# TreePy

## How To Install

### MacOS/Linux
> Type: `pip3 install treePy` into a terminal and press enter.<br>
### Windows
> Type: `pip install treePy` into CMD and press enter.<br>

## TreePy Basics
```python
import TreePy as tp        # Imports TreePy.

root = tp.Node("root")     # Creates root node.
tree = tp.Tree(root)       # Creates linked tree.

node1 = tp.Node("node1")   # Creates another node.

tree.add(node1)            # Adds node1 to root node
node1_data = tree.get([0]) # Gets node at branch 0 from root

```

## What is TreePy
TreePy is an open source python which simplifies linked trees in python

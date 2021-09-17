# ViperTree

## TreePy Basics
```python
import viper.tree as vp    # Imports viperTree.

root = vp.Node("root")     # Creates root node.
tree = vp.Tree(root)       # Creates linked tree.

node1 = vp.Node("node1")   # Creates another node.

tree.add(node1)            # Adds node1 to root node
node1_data = tree.get([0]) # Gets node at branch 0 from root

```

## What is ViperTree
ViperTree is an open source python which simplifies linked trees in python

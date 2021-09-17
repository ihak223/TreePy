# Node Object
class Node:
  def __init__(self, data):
    self.data = data
    self.source = None
    self.links = []
  def __repr__(self):
    return self.data
  def add(self, node):
    self.links.append(node)

# Tree Object  
class Tree:
  def __init__(self, root):
    self.root = root
    self.nodes = [root]
  def add(self, node):
    self.root.add(node)
  def get(self, coords):
    i = 0
    depth = len(coords)
    current_node = self.root
    while i != depth:
      current_node = current_node.links[coords[i]]

      i = i + 1
    return current_node
  def gadd(self, node, target_coords):
    target = self.get(target_coords)
    target.add(node)
    
    



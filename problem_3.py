# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

DELIMITER = ' '
LEAF_VAL = '#'

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
  def __str__(self):
    return self.val
  
def serialize(node):
  """
  Convert a node object into a string representation
  """
  ret_val = LEAF_VAL
  if node:
    ret_val = DELIMITER.join([str(node), serialize(node.left), serialize(node.right)])
  return ret_val

def deserialize(string):
  """
  - Split the string into a array using the delimiter as the separator
  - Take the first token as the root node
  - if leaf return None
  """
  
  tokens = string.split(DELIMITER)
  node = None

  val = tokens[0]
  if val == LEAF_VAL:
    return None

  node = Node(val)
  node.left = deserialize(DELIMITER.join(tokens[1:]))
  node.right = deserialize(DELIMITER.join(tokens[2:]))
  
  return node


node = Node('root', Node('left', Node('left.left')), Node('right'))

assert deserialize(serialize(node)).left.left.val == 'left.left'
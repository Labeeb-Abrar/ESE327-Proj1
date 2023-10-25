import random
from Node import Node

def create_random_tree(names, max_depth):

    root = Node(prefix=random.choice(names), children=[])
    for _ in range(random.randint(1, 3)):
        child_prefix = random.choice(names)
        child_count = random.randint(0, 10)
        root.children.append(Node(prefix=child_prefix, children=[], count=child_count))
    
    for child in root.children:
        create_random_children(child, names, max_depth)
    
    return root

def create_random_children(node, names, max_depth, current_depth=0):
    if current_depth > max_depth:
        return None
    
    for _ in range(random.randint(0, 3)):
        child_prefix = random.choice(names)
        child_count = random.randint(0, 10)
        node.children.append(Node(prefix=child_prefix, children=[], count=child_count))
        create_random_children(node.children[-1], names, max_depth, current_depth + 1)
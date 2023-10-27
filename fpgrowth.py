import matplotlib.pyplot as plt
from collections import Counter
from Node import Node

#create nodes for all of the items that we have in out dataset.


# when creating the first branch of the tree, we first need to make sure our list of transactions is sorted based on the support count.
# This function returns a tree (contained inside a node), the return var type is a Node class.
# Parameters: "transactions" is the transaction database D
#             "root" is the Node passed to create the Tree
#             "min_support" is the minimum support used to prune the transaction database based on support count
#   returns a frequent item dictionary

class FPTree:
    def __init__(self):
        self.tree_root = Node()
        self.header = {}    # create a dictionary that maps strings to linked lists, and the whole dictionary can be hashed and used as a key in another dict or set
    
    def getRoot(self):
        return self.tree_root
    
    def getHeader(self):
        return self.header
    
    #   add node to the header dict, this is the header list
    def addHeaderNode(self, Node):
        if Node.data is not None:
            if Node.data not in self.header:
                self.header[Node.data] = list()
                self.header[Node.data].append(Node)
            elif Node.data in self.header:
                self.header[Node.data].append(Node)
            
            print("self.header: ", self.header[Node.data])
        return

    def create_tree(self, transactions, min_support):
        sorted_frequent_items_dict = self.get_frequency_dict_from_transaction(transactions) # generate_frequency_dict(data=transactions, min_support=min_support)
        root = self.tree_root
        for transaction in transactions:
            transaction = sorted(transaction, key=lambda x: sorted_frequent_items_dict[x], reverse=True) #Sort our transaction list based on support counts
            current = root
            print(transaction)
            #adding transaction to tree
            for item in transaction:
                if sorted_frequent_items_dict[item] >= min_support: # min support threshold
                    if current.isItemChild(item):
                        child = current.getChild(item)   # find index of the item
                        child.count += 1
                        current = child
                    else:
                        current.children.append(Node(data=item, children=[], count=1, parent=current))
                        current = current.children[-1]
                        self.addHeaderNode(current) # for every new node created, it should be hashed in to the header
        return
    #   helper function
    def get_frequency_dict_from_transaction(self, transactions):
        freq = {}
        for t in transactions:
            for item in t:
                if item not in freq:
                    freq[item] = 1
                else:
                    freq[item] += 1
        return freq
    def get_frequency_dict_from_single_transaction(self, transaction):
        freq = {}
        for item in transaction:
            if item not in freq:
                freq[item] = 1
            else:
                freq[item] += 1
        return freq
    
    def add_transaction(self, transaction):
    # Sort transaction items based on frequency
     sorted_frequent_item_dict = self.get_frequency_dict_from_single_transaction(transactions)
     sorted_transaction = sorted(transaction, key=lambda x: sorted_frequent_item_dict[x], reverse=True)
    # Add transaction to the tree 
     current = self.root
     for item in sorted_transaction:
        if current.has_child(item):
           child = current.get_child(item)
           child.count += 1
        else:
           child = Node(item, 1) 
           current.add_child(child)
           self.add_header_node(child)

        current = child
    
    def find_prefix_paths(self, item):
     paths = []
     for node in self.header[item]:
        path = []
        while node and node.parent:
            path.append(node.data)
            node = node.parent  
        paths.append(path)
        return paths

    def build_conditional_tree(self, paths):
     tree = FPTree()
     for path in paths:
       # treat each path as a transaction
       tree.add_transaction(path) 
     return tree

    def is_single_path(self):
     """Check if tree contains only a single path"""
     if len(self.getRoot().children) == 1:
      return self.had_single_path(self.getRoot())
     else:
      return False

    def had_single_path(self, node:Node):
     """Recursively check if node has only one child"""
     if len(node.children) == 1:
       return self.had_single_path(node.children[0])
     elif len(node.children) == 0: 
       return True
     else:
       return False
     
    def get_single_path(self):
     if not self.is_single_path():
        return None

     # Follow nodes until reach leaf 
     path = []
     node = self.getRoot()
     while node:
        path.append(node.data)
        node = node.children[0]

     return path
     
    def generate_combinations(self, path, suffix):
     patterns = []
     for i in range(len(path)):
       pattern = path[i:] + suffix
       patterns.append(pattern)
     return patterns

    def mine_tree(self, suffix=[]):
     patterns = []
     for item in self.header:
       prefix_paths = self.find_prefix_paths(item)
       cond_tree = self.build_conditional_tree(prefix_paths)

       if cond_tree.is_single_path():  
          cond_patterns = self.generate_combinations(cond_tree.get_single_path, [item] + suffix)
       else:
          cond_patterns = cond_tree.mine_tree([item] + suffix)
      
       patterns.extend(cond_patterns)
     return patterns
    

  
    #   string output
    def __repr__(self) -> str:
        return f"{self.tree_root}"

transactions=[

    ["C", "B", "E", "G"],
    ["D", "C", "B"],
    ["A", "C", "D", "F"],
    ["D", "E", "F"],
    ["G", "C", "E", "F"],
]

fptree = FPTree()
min_support = 2
fptree.create_tree(transactions=transactions, min_support=min_support)
print(fptree)
print(fptree.header)
















"""
Creates a pyplot tree visualization
"""
def plot_tree(node, x, y, width, level):
    if node:
        plt.text(x, y, f"{node.data}\nCount: {node.count}", ha='center', va='center', bbox=dict(facecolor='white'))
        if level > 0:
            for child in node.children:
                dx = width / len(node.children)
                x_next = x - (width / 2) + dx / 2 + node.children.index(child) * dx
                y_next = y - 1.5  # Adjust vertical separation as needed
                plt.plot([x, x_next], [y, y_next], color='black', lw=2)
                plot_tree(child, x_next, y_next, dx, level - 1)
plt.figure(figsize=(8, 4))
plt.axis('off')
plot_tree(fptree.getRoot(), x=0, y=0, width=10, level=4)
plt.show()
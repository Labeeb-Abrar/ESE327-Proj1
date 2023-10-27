import matplotlib.pyplot as plt
from collections import Counter
from Node import Node

#create nodes for all of the items that we have in out dataset.
#Build a tree based off of the transactions dataset.
#If there are any nodes below or support count, remove the node/ that item all together. (from the dataset)
#An FP-tree is then constructed as follows. First, create the root of the tree, labeled
# with “null.” Scan database D a second time. The items in each transaction are processed
# in L order (i.e., sorted according to descending support count), and a branch is created
# for each transaction. For example, the scan of the first transaction, “T100: I1, I2, I5,”
# which contains three items (I2, I1, I5 in L order), leads to the construction of the first
# branch of the tree with three nodes, hI2: 1i, hI1: 1i, and hI5: 1i, where I2 is linked as a
# child to the root, I1 is linked to I2, and I5 is linked to I1. The second transaction, T200,
# contains the items I2 and I4 in L order, which would result in a branch where I2 is linked
# to the root and I4 is linked to I2. However, this branch would share a common prefix,
# I2, with the existing path for T100. Therefore, we instead increment the count of the I2
# node by 1, and create a new node, hI4: 1i, which is linked as a child to hI2: 2i.


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
            
            print("")
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
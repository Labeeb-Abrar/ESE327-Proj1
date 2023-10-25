import matplotlib.pyplot as plt
from collections import Counter
from Node import Node

#   returns a frequent item dictionary
def get_frequency_dict_from_transaction(transactions):
    freq = {}
    for t in transactions:
        for item in t:
            if item not in freq:
                freq[item] = 1
            else:
                freq[item] += 1
    return freq



# # Sample 2D array
# data = [
#     ["A", "B", "F", "G"],
#     ["D", "C", "B", "B"],
#     ["B", "C", "B", "G"],
#     ["C", "B", "G", "G"],
#     ["D", "E", "E", "B"]
# ]

# # Flatten the 2D array to get a list of items
# flat_data = [item for sublist in data for item in sublist]

# # Set a minimum support count threshold
# min_support = 2

# # Calculate the support counts
# item_counts = Counter(flat_data)
# # Collect frequent items (F)
# frequent_items = {item: count for item, count in item_counts.items() if count >= min_support}

# # Sort F by support count in descending order to get L
# sorted_frequent_items = sorted(frequent_items.items(), key=lambda x: x[1], reverse=True)
# sorted_frequent_items_dict = dict(sorted_frequent_items)
# print(sorted_frequent_items)
# print(sorted_frequent_items_dict)

"""
generates sorted dictionary with support counts of given database
"""
def generate_frequency_dict(data, min_support):
    flat_data = [item for sublist in data for item in sublist]
    # Calculate the support counts
    item_counts = Counter(flat_data)
    print(type(item_counts))
    # Collect frequent items (F)
    frequent_items = {item: count for item, count in item_counts.items() if count >= min_support}
    print(type(frequent_items))        
    # Sort F by support count in descending order to get L
    sorted_frequent_items = sorted(frequent_items.items(), key=lambda x: x[1], reverse=True)
    sorted_frequent_items_dict = dict(sorted_frequent_items)
    print(sorted_frequent_items)
    print(sorted_frequent_items_dict)

    return sorted_frequent_items_dict
# Print the list of frequent items L and their support counts
# for item, count in sorted_frequent_items:
#     print(f"Item: {item}, Support Count: {count}")
#print(type(sorted_frequent_items_dict))

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
def create_tree(transactions, root, min_support):
    sorted_frequent_items_dict = get_frequency_dict_from_transaction(transactions) # generate_frequency_dict(data=transactions, min_support=min_support)

    for transaction in transactions:
        transaction = sorted(transaction, key=lambda x: sorted_frequent_items_dict[x], reverse=True) #Sort our transaction list based on support counts
        current = root
        print(transaction)
        for item in transaction:
            if sorted_frequent_items_dict[item] >= min_support: # min support threshold
                if item in current.children:
                    #print("found")
                    current.children[item].count += 1
                    current = current.children[item]
                else:
                    current.children.append(Node(data=item, children=[], count=1, parent=current))
                    current = current.children[-1]
       # current = root
    return root

transactions=[

    ["C", "B", "E", "G"],
    ["D", "C", "B"],
    ["A", "C", "D", "F"],
    ["D", "E", "F"],
    ["G", "C", "E", "F"],
]

root = Node(data="null", children=[], count=0, parent=None)
frequency = get_frequency_dict_from_transaction(transactions)
print(frequency)
sorted_f = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
print(sorted_f)

min_support = 2
root = create_tree(transactions=transactions, root=root, min_support=min_support)
print(root)
# #   Remove elements not in the sorted frequent list
# for i in data:
#     for j in i:
#         deleteFlag = True
#         for item, count in sorted_frequent_items:
#             if item == j:
#                 deleteFlag = False
#         if deleteFlag:
#             i.remove(j)

# print(data)
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
plt.figure(figsize=(10, 6))
plt.axis('off')
plot_tree(root, x=0, y=0, width=10, level=4)
plt.show()
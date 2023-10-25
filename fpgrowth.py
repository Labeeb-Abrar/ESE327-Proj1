from Node import Node
import matplotlib.pyplot as plt

# Sample Database
# ('B', 7), ('G', 4), ('C', 3), ('D', 2), ('E', 2)
# B G C D E A F
# each set is a transaction
D = [
    ["B", "E", "A", "F"],
    ["C", "E", "A"]
    # ["C", "E", "F"],
    # ["G", "D", "E", "A"],
    # ["G", "C", "E"]
]
tree_depth = 3  # for tree plot
"""
FP Growth algorithm:
- for each transaction:
    - append lol
"""
root = Node("null")

for transaction in D:
    current = root
    for item in transaction:
        if not current.isItemChild(item):
            node = Node(item)
            current.children.append(node)
            current = node
        else:
            # current = current.children.index(item)
            current.count += 1

print(root)
def plot_tree(node, x, y, width, level):
    if node:
        plt.text(x, y, f"{node.prefix}\nCount: {node.count}", ha='center', va='center', bbox=dict(facecolor='white'))
        if level > 0:
            for child in node.children:
                dx = width / len(node.children)
                x_next = x - (width / 2) + dx / 2 + node.children.index(child) * dx
                y_next = y - 1.5  # Adjust vertical separation as needed
                plt.plot([x, x_next], [y, y_next], color='black', lw=2)
                plot_tree(child, x_next, y_next, dx, level - 1)
plt.figure(figsize=(10, 6))
plt.axis('off')
plot_tree(root, x=0, y=0, width=10, level=1)
plt.show()
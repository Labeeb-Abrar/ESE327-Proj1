from randomTree import create_random_tree
import matplotlib.pyplot as plt

names = ["A", "B", "C", "D", "E", "F", "G"]
max_depth = 3  # Adjust the maximum depth as needed.
root = create_random_tree(names, max_depth)
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
plot_tree(root, x=0, y=0, width=10, level=max_depth)
# plt.show()

header = []

def level_order_traversal(root):
    if root is None:
        return
    
    for child in root.children:
        # print(f"[{i.prefix}, {i.count}]", end=' ')
        if child is not None:
            if child.prefix not in header:
                header.append([child])
            else:
                for i in header:
                    if i[0].prefix == child.prefix:
                        i.append(child)
    queue = root.children

    while queue:
        node = queue.pop(0)
        level_order_traversal(node)
        
level_order_traversal(root)
print(header)
plt.show()
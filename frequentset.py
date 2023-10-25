
###### THIS IS FOR TESTING PURPOSES #######
# import random

# alphabet_choices = ["A", "B", "C", "D", "E", "F", "G"]  # Define the alphabet choices
# data = [[random.choice(alphabet_choices) for _ in range(20)] for _ in range(5)]   # Create the 5x20 2D array with random alphabets
# for row in data:  # Print the 2D array
#     print(row)


from collections import Counter

# Sample 2D array
data = [
    ["A", "B", "F", "G"],
    ["D", "C", "B", "B"],
    ["B", "C", "B", "G"],
    ["C", "B", "G", "G"],
    ["D", "E", "E", "B"]
]

# Flatten the 2D array to get a list of items
flat_data = [item for sublist in data for item in sublist]

# Set a minimum support count threshold
min_support = 2

# Calculate the support counts
item_counts = Counter(flat_data)
# Collect frequent items (F)
frequent_items = {item: count for item, count in item_counts.items() if count >= min_support}

# Sort F by support count in descending order to get L
sorted_frequent_items = sorted(frequent_items.items(), key=lambda x: x[1], reverse=True)
print(sorted_frequent_items)
class Node:
    def __init__(self, prefix=None, count=0, children=[]) -> None:
        self.count = count
        self.prefix = prefix
        self.children = children
        return
    def __str__(self):
        return f"{self.prefix} --> {self.children}"
    
    def isItemChild(self, item):
        if len(self.children) == 0:
            return False
        
        for node in self.children:
            if node.prefix == item:
                return True
        return False
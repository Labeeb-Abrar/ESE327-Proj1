class Node:
    def __init__(self, prefix=None, count=0, children=[]) -> None:
        self.count = count
        self.prefix = prefix
        self.children = children
        return
    def __repr__(self) -> str:
        return f"{self.prefix} --> {self.children}"
    
    """
    Checks if the item (node data/prefix) is present inside children
    """
    def isItemChild(self, item):
        if len(self.children) == 0:
            return False
        
        for node in self.children:
            if node.prefix == item:
                return True
        return False
class Node:
    def __init__(self, data=None, count=0, children=[], parent=None) -> None:
        self.count = count
        self.data = data
        self.children = children
        self.parent = parent
        self.header_link = None
        return
    def __repr__(self) -> str:
        return f"{self.data}:{self.count} --> {self.children}"
    
    """
    Checks if the item (node data/prefix) is present inside children
    """
    def isItemChild(self, item):
        if len(self.children) == 0:
            return False
        
        for node in self.children:
            if node.data == item:
                return True
        return False
    def getChild(self, item):
        for node in self.children:
            if node.data == item:
                return node
        return None
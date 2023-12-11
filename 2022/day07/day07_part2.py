import sys

class Tree:
    def __init__ (self, name = "root", type = "dir", parent = None, children=None, value = 0):
        self.name = name
        self.type = type
        self.parent = parent
        self.children = []
        self.value = value
        if children != None:
            for child in children:
                self.add_child(child)
    
    def get_type(self):
        return self.type
    
    def get_name(self):
        return self.name
    
    def get_child(self, name):
        childrenNames = [child.get_name() for child in self.get_children()]
        i = childrenNames.index(name)
        return self.children[i]
    
    def get_children(self):
        return self.children
    
    def get_parent(self):
        return self.parent
    
    def get_value(self):
        return self.value
    
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

    def add_value(self, v: int):
        self.value += v

    def add_parent(self, parentNode):
        assert isinstance(parentNode, Tree)
        self.parent = parentNode

    def __str__(self):
        return self.name


def parseCommand(line: str, currentNode: Tree):
    if (line.find('cd') != -1): 
        if (line.find('/') != -1): # root node
            return currentNode
        elif (line.find('..') != -1):
            currentNode = currentNode.get_parent()
        else:
            currentNode = currentNode.get_child(line.split()[2])

    return currentNode
    
def parseLS(line: str, currentNode: Tree):
    if (line.find('dir') != -1): 
        value = 0
        name = line.split()[1]
        type = "dir"
    else:
        value = int(line.split()[0])
        name = line.split()[1]
        type = "file"

    parent = currentNode
    node = Tree(name, type, parent, None, value)
    currentNode.add_child(node)
    currentNode.add_value(value)
    
    while (currentNode.get_parent() != None and currentNode.get_type() == "dir"):
        currentNode = currentNode.get_parent()
        currentNode.add_value(value)

def getDeletedDirSize(remainingSpace: int, currentNode: Tree, directorySize: int):
    targetSize = 30_000_000
    curDirectorySize = 70_000_000

    value = currentNode.get_value() 
    if (remainingSpace + value >= targetSize):
        curDirectorySize = min(value, directorySize)

    for child in currentNode.get_children():
        if (child.get_type() == "dir"):
            curDirectorySize = min(curDirectorySize, getDeletedDirSize(remainingSpace, child, curDirectorySize))
    
    return curDirectorySize


if __name__ == "__main__":
    input = open(sys.argv[1]).read().split("\n")
    
    root = Tree()
    currentNode = root

    for line in input:
        if line[0] == '$': # command
            currentNode = parseCommand(line, currentNode)
        else: # the result from ls is being shown
            parseLS(line, currentNode)

    totalSpace = 70_000_000
    remainingSpace = totalSpace - root.get_value()

    directorySize = getDeletedDirSize(remainingSpace, root, root.get_value())

    print(f"The sum of the total sizes of the directories of at most 100000 is {directorySize}")
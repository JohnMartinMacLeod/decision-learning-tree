from entropy import *
from classes import TreeNode

# Returns column name with highest information gain, and it's information gain
def findBestColumn(data: list, columns: dict):
    bestColumn = None
    bestInfoGain = 0

    for columnName, values in columns.items():
            
        infoGain = calculateIG(h_current(data),h_after(data, columnName, values))

        if infoGain > bestInfoGain:
            bestColumn = columnName
            bestInfoGain = infoGain
    
    return bestColumn, bestInfoGain


# Recursively builds a tree from a dataset data, dictionary columns, and list of classifier values classifierValuesList 
def searchTree(data: list, columns: dict, classifierValuesList: list):

    allSameBool, classifierName = allSameClassifier(data)

    if allSameBool:

        return TreeNode(classifier = classifierName)
    
    if not columns:

        mostCommon = mostCommonClassifier(data, classifierValuesList)

        return TreeNode(classifier = mostCommon)
    
    bestColumn, bestInfoGain = findBestColumn(data, columns)

    if bestInfoGain == 0:
        mostCommon = mostCommonClassifier(data, classifierValuesList)
        return TreeNode(classifier = mostCommon)
    
    node = TreeNode(column = bestColumn)

    for value in columns[bestColumn]:
        subtree = []
        for row in data:
            if getattr(row, bestColumn) == value:
                subtree.append(row)


        if not subtree:
            node.children[value] = TreeNode(classifier = mostCommonClassifier(data, classifierValuesList))

        if subtree:
            newColumns = columns.copy()
            del newColumns[bestColumn]
            node.children[value] = searchTree(subtree, newColumns, classifierValuesList)

    return  node

# Returns whether dataset data contains all of the same classifier
def allSameClassifier(data: list):
    classifierList = []
    for row in data:
        classifierList.append(row.classifier)
    if len(set(classifierList)) == 1:
        return (True, classifierList[0])
    else:
        return (False, None)
    
# Returns the most common classifier in dataset data
def mostCommonClassifier(data: list, classifierValuesList: list): 
    mostCommon = []
    for i in range(len(classifierValuesList)):
        count = 0
        for row in data:
            if row.classifier == classifierValuesList[i]:
                count += 1
        mostCommon.append((count, classifierValuesList[i]))

    mostCommon.sort(reverse = True)

    return mostCommon[0][1]


# Prints a visual representation of a tree
def printTree(node: TreeNode, indent=""):
    if node.classifier is not None:
        print(indent + f"-> {node.classifier}")
        return
    
    print(indent + f"[{node.column}]")
    
    for value, child in node.children.items():
        print(indent + f" ├── {value}:")
        printTree(child, indent + " │   ")

# Predicts the classifier of an object car given a decision tree tree 
def predict(tree: TreeNode, car: object):
    node = tree
    while node != None and node.classifier == None: 
        column = node.column
        if column == None:
            return None
        val = getattr(car, column)

        if val in node.children:
            node = node.children[val]
        else:
            return node.classifier
    
    
    return node.classifier if node is not None else None


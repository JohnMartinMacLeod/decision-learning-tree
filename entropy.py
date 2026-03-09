import math
from constants import *

#Calculate entropy of column col at value val in dataset data. Type is the type of entropy you want to calculate either "current" or "after"
def calculateEntropy(data: list, col: str, val: str, type: str = "current"): 

    p = []
    h = 0

    if type == "current":
        classCountList = createClassCountList(data)
        for i in range(NUM_CLASSIFIER_VALS):
            p.append((classCountList[i] / len(data)))

    if type == "after":
        columnValueList = createColumnValueList(data, col, val)
        classCountList = createClassCountList(columnValueList)
        for i in range(len(classCountList)):
            if len(columnValueList) == 0:
                continue
            else:
                p.append((classCountList[i] / len(columnValueList)))

    for i in range(len(p)):
        
        if p[i] > 0:
            h -= p[i] * math.log2(p[i])
        else:
            pass

    return h

# Calculates entropy of the current dataset
def h_current(data: list):
    return calculateEntropy(data, None, None, "current")

# Calculates entropy after a potential split
def h_after(data: list, col: str, val: str):
    h = []
    columnValueList = []
    h_after = 0

    for i in range(len(val)):
        columnValueList.append(createColumnValueList(data, col, val[i]))
        h.append(calculateEntropy(data, col, val[i], "after"))

    for i in range(len(h)):
        h_after += h[i] * (len(columnValueList[i]) / len(data))

    return h_after


# Return a list of values val contained in dataset data at column col
def createColumnValueList(data: list, col: str, val: str): 
    columnValueList = []
    for i in data:
        if getattr(i, col) == val:
            columnValueList.append(i)
    return columnValueList


# Will return a list containing quantity of each classifier in given list
def createClassCountList(data): 
        pUnacc = 0
        pAcc = 0
        pGood = 0
        pVeryGood = 0
        for element in data:
            if element.classifier == "unacc":
                pUnacc += 1
            elif element.classifier == "acc":
                pAcc += 1
            elif element.classifier == "good":
                pGood += 1
            elif element.classifier == "vgood":
                pVeryGood += 1
            else:
                raise ValueError("Class column in dataset must contain either 'unacc', 'acc', 'good', or 'vgood'")
        
        p = [pUnacc, pAcc, pGood, pVeryGood]
        return p


# Calculate information gain
def calculateIG(h_current, h_after):
    return (h_current - h_after)


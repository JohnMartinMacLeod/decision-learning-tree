from fileReader import *
import random
from constants import *
from entropy import *
from searchTree import *



cars, header, columns, classifierValuesList = readCSV('car.csv')

random.shuffle(cars)
split = int(TRAIN_DATA_PERCENT * len(cars))
trainingData = cars[:split]
testingData = cars[split:]

tree = searchTree(trainingData, columns, classifierValuesList)
print("Visualised Tree")
printTree(tree)

for row in testingData:
    print("Car is predicted to be:", predict(tree, row))

import csv
from classes import Car


# Return given csv file as a list of car objects table, a list of the files headers, a dictionary of all the headers and their values, and a list of all unique classifiers
def readCSV(fileName: str):
    with open(fileName, mode='r', newline='') as file:
        f = csv.reader(file)
        header = next(f)
        columns = {}
        table = []
        classifierValuesList = []

        for cols in header[:-1]: 
            columns[cols] = set()

        for row in f:
            for i, cols in enumerate(header[:-1]):
                columns[cols].add(row[i])
            table.append(Car(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
            
        for cols in columns:
            columns[cols] = list(columns[cols])

        for cars in table:
            classifierValuesList.append(cars.classifier)

    return table, header, columns, list(set(classifierValuesList))


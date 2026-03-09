class Car():
    def __init__(self, price, upkeep, doors, personCapacity, luggageCapacity, safety, classifier):
        self.price = price
        self.upkeep = upkeep
        self.doors = doors
        self.personCapacity = personCapacity
        self.luggageCapacity = luggageCapacity
        self.safety = safety
        self.classifier = classifier


class TreeNode():
    def __init__(self, column = None, value = None, children = None, classifier = None):
        self.column = column
        self.value = value
        if children == None:
            self.children = {}
        else:
            self.children = children
        self.classifier = classifier
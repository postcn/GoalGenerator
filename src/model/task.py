class Task:

    def __init__(self, description, repititions):
        self.description = description
        self.repititions = repititions

    def getRepititions(self):
        return self.repititions

    def getDescription(self):
        return self.description

    def toDescription(self):
        return self.description.format(self.repititions)

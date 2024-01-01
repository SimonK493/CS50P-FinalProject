class Exercise:
    def __init__(self, name, weight = 0, repetitions = 0):
        self.name = name
        self.weight = weight
        self.repetitions = repetitions
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            return False
        else:
            self._name = name
        

e = Exercise("Übung 1")

e.name = "ddd"

print(e.name)

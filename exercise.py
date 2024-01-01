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

    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, weight):
        if weight >= 0:
            self._weight = weight

    @property
    def repetitions(self):
        return self._repetitions
    
    @repetitions.setter
    def repetitions(self, repetitions):
        if repetitions >= 0:
            self._repetitions = repetitions
        

from time1 import Time


class Section:
    def __init__(self, name: int or str, start: Time, end: Time):
        if type(name) is int:
            self.name = "Period " + str(name)
        else:
            self.name = name
        self.start = start
        self.end = end

    def __str__(self):
        return self.name + ": " + str(self.start) + " - " + str(self.end)

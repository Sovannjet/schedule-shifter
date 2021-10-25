class Time:
    def __init__(self, h: int, m: int):
        self.hr = h
        self.min = m

    def add(self, m):
        new_time = Time(self.hr, self.min)
        new_time.min += m
        if new_time.min > 59:
            new_time.hr += new_time.min // 60
            new_time.min %= 60
            if new_time.hr > 12:
                new_time.hr %= 12

        return new_time

    def __str__(self):
        minutes = str(self.min)
        if self.min < 10:
            minutes = "0" + minutes

        return str(self.hr) + ":" + minutes

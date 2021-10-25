from time1 import Time
from section import Section


class Schedule:
    def __init__(self, name: str,
                 start: Time, period_len: int, passing_len: int, lunch: int, lunch_len: int, break_len: int,
                 sections: list):
        self.name = name
        self.start = start
        self.period_len = period_len
        self.passing_len = passing_len
        self.lunch = lunch
        self.lunch_len = lunch_len
        self.break_len = break_len
        self.sections = sections

        self.sched = []
        for i in range(len(sections)):
            if i == 0:
                self.sched.append(Section(sections[i], self.start, self.start.add(self.period_len)))
            else:
                start = self.sched[i - 1].end.add(self.passing_len)
                if type(sections[i]) is int:
                    self.sched.append(Section(sections[i], start, start.add(self.period_len)))
                elif sections[i] == "A-TECH Time":
                    self.sched.append(Section(sections[i], start, start.add(self.break_len)))
                elif sections[i] == "Lunch":
                    start = start.add(-self.passing_len)  # no passing period to lunch
                    self.sched.append(Section(sections[i], start, start.add(self.lunch_len)))

    def offset(self, offset: int):
        schedule = Schedule(self.name,
                            self.start, self.period_len + offset, self.passing_len,
                            self.lunch, self.lunch_len, self.break_len,
                            self.sections)
        return schedule

    def __str__(self):
        schedule = self.name + "\n"
        for sec in self.sched:
            schedule += str(sec) + "\n"
        return schedule

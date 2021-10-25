from time1 import Time
from schedule import Schedule

START_TIME = Time(7, 25)
BLOCK_PER_LEN = 80
COMMON_PER_LEN = 42
PASSING_PER_LEN = 4
BLOCK_LUN_LEN = 30
COMMON_LUN_LEN = 41
ATECH_TIME_LEN = 39

aday_sections = (1, 3, "A-TECH Time", 5, "Lunch", 7)
bday_sections = (2, 4, "A-TECH Time", "Lunch", 6, 8)
cday_sections = (1, 2, 3, 4, 5, "Lunch", 6, 7, 8)

aday = Schedule("A-Day", START_TIME, BLOCK_PER_LEN, PASSING_PER_LEN, 2, BLOCK_LUN_LEN, ATECH_TIME_LEN, aday_sections)
bday = Schedule("B-Day", START_TIME, BLOCK_PER_LEN, PASSING_PER_LEN, 1, BLOCK_LUN_LEN, ATECH_TIME_LEN, bday_sections)
cday = Schedule("C-Day", START_TIME, COMMON_PER_LEN, PASSING_PER_LEN, 2, COMMON_LUN_LEN, 0, cday_sections)

offset = int(input("How many minutes do you want to add to each period? (use a negative number to shorten periods) "))

print(aday.offset(offset))
print(bday.offset(offset))
print(cday.offset(offset))

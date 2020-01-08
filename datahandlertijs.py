import datetime
import shutil
import time
import os
import extras

conststr = "(SkyblockCompetitive) (me » itepastra) "
newblock = 0
vals = []
hpet = []
# hoi

with open(extras.filepath("gegevens.txt"), "r") as file:
    data = file.readlines()
    for index, line in enumerate(data):
        if line == "\n":
            newblock = 0
        else:
            value = extras.texttonum(line)
            if newblock == 0:
                vals.append(value)
                hpet.append(0)
            elif newblock == 1:
                hpet[-1] = value
            newblock += 1

for val, pet in zip(vals, hpet):
    print(val, pet)

print(len(vals), len(hpet))

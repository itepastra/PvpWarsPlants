import datetime
import shutil
import time
import os
import extras

conststr = "(SkyblockCompetitive) (me » itepastra) "
newblock = True
vals = []
with open(extras.filepath("gegevens.txt"), "r") as file:
    data = file.readlines()
    for line in data:
        if line == "\n":
            newblock = True
        if "[" in line:
            value = line.split("[CHAT] ", 1)[1]
            if "+" in value:
                value = value.split("+ $", 1)[1].split(" ", 1)[0].replace(",", "")
                if "M" in value:
                    value = int(float(value[0:-1]) * 1000000)
                elif "B" in value:
                    value = int(float(value[0:-1]) * 1000000000)
                else:
                    value = int(float(value))
                if newblock == True:
                    vals.append(value)
                newblock = False

print(vals)

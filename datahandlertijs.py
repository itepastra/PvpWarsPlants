import datetime
import shutil
import time
import os
import extras

conststr = "(SkyblockCompetitive)"
newblock = 0
vals = []
hpet = []
seeds = extras.input_("seeds.json")
seedtype = None
dellines = []

with open(extras.filepath("gegevens.txt"), "r") as file:
    data = file.readlines()
    for index, line in enumerate(data):
        if line == "\n":
            newblock = 0
            dellines.append(index)
        elif line.partition("[CHAT] ")[2].startswith(conststr):
            name, ending = line.split(" ")[-2:]
            long = extras.findseed(ending[:-1], seeds, "name")
            short = extras.findseed(ending[:-1], seeds, "nn")
            if name == "me)":
                print("not from me")
            elif long is not None:
                seedtype = long
            elif short is not None:
                seedtype = short
            elif ending == "stop":
                seedtype = None
        else:
            value = extras.texttonum(line)
            if index != 0:
                dellines.append(index)
            if newblock == 0 and seedtype is not None:
                print(seedtype, index, value)
                seeds = extras.addvals(seedtype, value)
                hpet.append(0)
            elif newblock == 1 and seedtype is not None:
                hpet[-1] = value
            newblock += 1

with open(extras.filepath("gegevens.txt"), "w") as file:
    for index in dellines:
        data[index] = ""
    file.writelines(data)
    file.writelines("\n")

for seed in seeds:
    print(seed["name"], seed["values"])

extras.output("seeds2.json", seeds)

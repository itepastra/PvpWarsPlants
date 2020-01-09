import datetime
import shutil
import time
import os
import extras

conststr = "Render thread/INFO"
lenstr = len(conststr)
docopy = True


def pend(data, index):
    temp = ["\n"]
    amt = 0
    plus = True
    i = index
    while (
        data[i][11 : 27 + lenstr] == "[" + conststr + "]: [CHAT] [!] R"
        or data[i][11 : 27 + lenstr] == "[" + conststr + "]: [CHAT] [!] D"
        or data[i][11 : 25 + lenstr] == "[" + conststr + "]: [CHAT] (!)"
        or data[i][11 : 26 + lenstr] == "[" + conststr + "]: [CHAT]  + $"
    ):
        if not data[i][11 : 26 + lenstr] == "[" + conststr + "]: [CHAT]  + $":
            plus = False

        elif (
            plus == False
            and data[i][11 : 26 + lenstr] == "[" + conststr + "]: [CHAT]  + $"
        ):
            temp.append("\n")
            plus = True

        temp.append(data[i])
        amt += 1
        i += 1
    if i == index:
        temp = []
    return temp, amt


harvests = []
savelines = 0
amt = 0

if docopy:
    shutil.copyfile(
        "D:/losse spellen/MultiMC/instances/Vanilla/.minecraft/logs/latest.log",
        extras.filepath("log.txt"),
    )
early = True
n = 0
i = 0


with open(extras.filepath("gegevens.txt"), "r") as gegevens:
    timestr = gegevens.readline()
    latetime = datetime.datetime.fromisoformat(timestr)
    today = datetime.datetime.today()


with open(extras.filepath("log.txt"), "r") as file:
    data = file.readlines()

    while early:
        if data[i].startswith("["):
            line = data[i][1:9]
            time = datetime.datetime.strptime(line, "%H:%M:%S").replace(
                year=today.year(), month=today.month(), day=today.day()
            )
            if time > latetime:
                early = False
        i += 1

    for index, line in enumerate(data):
        if index <= i:
            pass
        elif amt > 1 or len(line) <= 25 + lenstr:
            amt -= 1
        elif line[23 + lenstr] == "+":
            temp, amt = pend(data, index)
            harvests.extend(temp)
        elif line.partition("[CHAT] (SkyblockCompetitive)")[2] != "":
            harvests.extend(["\n", line])


with open(extras.filepath("gegevens.txt"), "a") as save:
    print("klaar")
    save.write(datetime.datetime.isoformat(datetime.datetime.now()))
    save.write("".join(harvests))

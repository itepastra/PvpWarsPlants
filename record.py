import datetime
import shutil
import time
import os
import data

conststr = "Render thread/INFO"
lenstr = len(conststr)


def filepath(
    filename
):  # deze functie geeft het path van het bestand zelf terug hoe je het ook
    # uitvoert, zodat het programma het bestand goed kan vinden
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, filename)


def pend(data, index):
    temp = []
    amt = 0
    i = index
    while (
        data[i][11 : 27 + lenstr] == "[" + conststr + "]: [CHAT] [!] R"
        or data[i][11 : 27 + lenstr] == "[" + conststr + "]: [CHAT] [!] D"
        or data[i][11 : 25 + lenstr] == "[" + conststr + "]: [CHAT] (!)"
        or data[i][11 : 26 + lenstr] == "[" + conststr + "]: [CHAT]  + $"
    ):
        temp.append(data[i])
        amt += 1
        i += 1
    if i != index:
        temp.append("\n")
    return temp, amt


harvests = []
savelines = 0
amt = 0
shutil.copyfile(
    "D:/losse spellen/MultiMC/instances/Vanilla/.minecraft/logs/latest.log",
    filepath("log.txt"),
)
early = True
n = 0
i = 0


with open(filepath("gegevens.txt"), "r") as gegevens:
    zin = gegevens.readlines()[-2][1:9]
    try:
        latetime = datetime.datetime.strptime(zin, "%H:%M:%S")
    except ValueError:
        pass


with open(filepath("log.txt"), "r") as file:
    data = file.readlines()

    while early:
        line = data[i][1:9]
        try:
            time = datetime.datetime.strptime(line, "%H:%M:%S")
        except ValueError:
            pass
        print(time, latetime)
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


with open(filepath("gegevens.txt"), "a") as save:
    print("klaar")
    save.write("".join(harvests))

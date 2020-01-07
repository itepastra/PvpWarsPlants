import datetime
import shutil
import time
import os

conststr = "Render thread/INFO"
lenstr = len(conststr)

cactus =
avocado
sewerfruit
netherfruit
bamboo
hamburger
seafruit
lemon
coconut




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
        data[i][11:45] == "[" + conststr + "]: [CHAT] [!] R"
        or data[i][11:45] == "[" + conststr + "]: [CHAT] [!] D"
        or data[i][11:43] == "[" + conststr + "]: [CHAT] (!)"
        or data[i][11:44] == "[" + conststr + "]: [CHAT]  + $"
    ):
        temp.append(data[i])
        amt += 1
        i += 1
    if i != index:
        temp.append("\n")
    return temp, amt


harvests = []
# while True:
savelines = 0
amt = 0
shutil.copyfile(
    "D:/losse spellen/MultiMC/instances/Vanilla/.minecraft/logs/latest.log",
    filepath("log.txt")
)
early = True
n = 0
with open(filepath('log.txt'), "r") as file:
    data = file.readlines()
    while early:

        if line[2:11]:

    for index, line in enumerate(data):
        if amt > 1 or len(line) <= 42:
            amt -= 1
        elif line[41] == "+":
            temp, amt = pend(data, index)
            harvests.extend(temp)


with open(filepath("gegevens.txt"), "a") as save:
    print("klaar")
    save.write("".join(harvests))

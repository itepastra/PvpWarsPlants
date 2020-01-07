import datetime
import shutil
import time
import os

conststr = "Render thread/INFO"
lenstr = len(conststr)

cactus ={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
avocado = {"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
sewerfruit= {"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
netherfruit= {"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
bamboo={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
hamburger={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
seafruit={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
lemon={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
coconut={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
pear = {"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
eggplant={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
apple={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
beetroot={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
bubblegum={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
slimereed={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
blazereed={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
rubybush={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
cherry={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
taco={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
chocolate={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
enderbloom={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
goldenapple={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
pumpkinpie={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
football={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
turkeytrap={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}
iceball={"name":"", "size":(0,0,0), "wateramt":0, "watertime":0, "totaltime": 0,}



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
            pass
    for index, line in enumerate(data):
        if amt > 1 or len(line) <= 42:
            amt -= 1
        elif line[41] == "+":
            temp, amt = pend(data, index)
            harvests.extend(temp)


with open(filepath("gegevens.txt"), "a") as save:
    print("klaar")
    save.write("".join(harvests))

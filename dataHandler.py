import datetime
import shutil
import time
import os
import extras

constPlants = {
    'Cactus',
    'Avocado',
    'Sewerfruit',
    'Netherfruit',
    'Seafruit',
    'Lemon',
    'Coconut',
    'Pear',
    'Eggplant',
    'Apple',
    'Beetroot',
    'Bubblegum',
    'Slimereed',
    'Blazereed',
    'Rubybush',
    'Cherry',
    'Taco',
    'Chocolate',
    'Enderbloom',
    'Goldenapple',
    'PumpkinPie',
    'FootBall',
    'TurkeyTrap',
    'IceBall'
}

Cactus = []
Avocado = []
Sewerfruit = []
Netherfruit = []
Seafruit = []
Lemon = []
Coconut = []
Pear = []
Eggplant = []
Apple = []
Beetroot = []
Bubblegum = []
Slimereed = []
Blazereed = []
Rubybush = []
Cherry = []
Taco = []
Chocolate = []
Enderbloom = []
Goldenapple = []
PumpkinPie = []
Football = []
TurkeyTrap = []
IceBall = []

def filepath(filename):  # deze functie geeft het path van het bestand zelf terug hoe je het ook uitvoert, zodat het programma het bestand goed kan vinden
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, filename)

def AddMoneyToSeedArray(Seed, Money):
    if Seed == "Cactus":
        Cactus.append(Money)
    elif Seed == "Avocado":
        Avocado.append(Money)
    elif Seed == "Sewerfruit":
        Sewerfruit.append(Money)
    elif Seed == "Netherfruit":
        Netherfruit.append(Money)
    elif Seed == "Seafruit":
        Seafruit.append(Money)
    elif Seed == "Lemon":
        Lemon.append(Money)
    elif Seed == "Coconut":
        Coconut.append(Money)
    elif Seed == "Pear":
        Pear.append(Money)
    elif Seed == "Eggplant":
        Eggplant.append(Money)
    elif Seed == "Apple":
        Apple.append(Money)
    elif Seed == "Beetroot":
        Beetroot.append(Money)
    elif Seed == "Bubblegum":
        Bubblegum.append(Money)
    elif Seed == "Slimereed":
        Slimereed.append(Money)
    elif Seed == "Blazereed":
        Blazereed.append(Money)
    elif Seed == "Rubybush":
        Rubybush.append(Money)
    elif Seed == "Cherry":
        Cherry.append(Money)
    elif Seed == "Taco":
        Taco.append(Money)
    elif Seed == "Chocolate":
        Chocolate.append(Money)
    elif Seed == "Enderbloom":
        Enderbloom.append(Money)
    elif Seed == "Goldenapple":
        Goldenapple.append(Money)
    elif Seed == "PumpkinPie":
        PumpkinPie.append(Money)
    elif Seed == "Football":
        Football.append(Money)
    elif Seed == "TurkeyTrap":
        TurkeyTrap.append(Money)
    elif Seed == "IceBall":
        IceBall.append(Money)

with open(filepath('gegevens.txt'), "r") as file:
    data = file.readlines()
    harvestedSeed = ""
    for line in data:
        if line != "\n":
            splitLine = line.split(" ")
            if(splitLine[3].startswith("(Sky")):
                for Seed in constPlants:
                    if splitLine[7].replace("\n", "").lower() == Seed.lower():
                        harvestedSeed = Seed
                        print(Seed + " has been started to be harvested")
                    elif splitLine[7].replace("\n", "").lower() == "stop":
                        harvestedSeed = ""
                        print("Last seed has been stopped harvesting")
            elif(splitLine[5].startswith("$")):
                noDollar = splitLine[5].split("$")[1]
                if(noDollar.endswith("B")):
                    AddMoneyToSeedArray(harvestedSeed, int(float(noDollar.split("B")[0]) * 1000000000))
                elif(noDollar.endswith("M")):
                    AddMoneyToSeedArray(harvestedSeed, int(float(noDollar.split("M")[0]) * 1000000))
                else:
                    AddMoneyToSeedArray(harvestedSeed, int(float(noDollar.replace(",", ""))))
print(Apple)
print(IceBall)

import datetime
import shutil
import time
import os
import extras

constCactus = "(SkyblockCompetitive) (me » itepastra) Cactus"
constAvocado = "(SkyblockCompetitive) (me » itepastra) Avocado"
constSewerfruit = "(SkyblockCompetitive) (me » itepastra) Sewerfruit"
constNetherfruit = "(SkyblockCompetitive) (me » itepastra) Netherfruit"
constHamburger = "(SkyblockCompetitive) (me » itepastra) Hamburger"
constSeafruit = "(SkyblockCompetitive) (me » itepastra) Seafruit"
constLemon = "(SkyblockCompetitive) (me » itepastra) Lemon"
constCoconut = "(SkyblockCompetitive) (me » itepastra) Cocunut"
constPear = "(SkyblockCompetitive) (me » itepastra) Pear"
constEggplant = "(SkyblockCompetitive) (me » itepastra) Eggplant"
constApple = "(SkyblockCompetitive) (me » itepastra) Apple"
constBeetroot = "(SkyblockCompetitive) (me » itepastra) Beetroot"
constBubblegum = "(SkyblockCompetitive) (me » itepastra) Bubblegum"
constSlimereed = "(SkyblockCompetitive) (me » itepastra) Slimereed"
constBlazereed = "(SkyblockCompetitive) (me » itepastra) Blazereed"
constRubybush = "(SkyblockCompetitive) (me » itepastra) Rubybush"
constCherry = "(SkyblockCompetitive) (me » itepastra) Cherry"
constTaco = "(SkyblockCompetitive) (me » itepastra) Taco"
constChocolate = "(SkyblockCompetitive) (me » itepastra) Chocolate"
constEnderbloom = "(SkyblockCompetitive) (me » itepastra) Enderbloom"
constGoldenapple = "(SkyblockCompetitive) (me » itepastra) Goldenapple"
constPumpkinpie = "(SkyblockCompetitive) (me » itepastra) Pumpkin pie"
constFootball = "(SkyblockCompetitive) (me » itepastra) FootBall"
constTurkeyTrap = "(SkyblockCompetitive) (me » itepastra) TurkeyTrap"
constIceBall = "(SkyblockCompetitive) (me » itepastra) IceBall"


with open(extras.filepath("gegevens.txt"), "r") as file:
    data = file.readlines()
    for line in data:
        splitLine = line.split(" ")
        print(splitLine[4])

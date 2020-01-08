import json
import os
import statistics
from typing import List, Dict, Any


def input_(filename):
    with open(filepath(filename)) as infile:
        return json.load(infile)


def output(filename, data):
    with open(filepath(filename), "w") as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)


def filepath(
    filename
):  # deze functie geeft het path van het bestand zelf terug hoe je het ook
    # uitvoert, zodat het programma het bestand goed kan vinden
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, filename)


def update(seeds):
    for seed in seeds:
        values = seed["values"]
        values.append(seed["averageworth"] * seed["amtfound"])
        print(values)
        mean = statistics.mean(values)
        stdev = statistics.stdev(values)
        seed["averageworth"] = mean
        seed["stdev"] = stdev
    return seeds


def addvals(
    seedtype: str,
    values: list,
    data: List[Dict[str, Any]] = input_("seeds.json"),
    skey: str = "nn",
    okey: str = "values",
):
    index = None
    for i, dic in enumerate(data):
        if dic[skey] == seedtype:
            index = i
    data[index][okey].extend(values)


def texttonum(text, before="[CHAT]  + $", after=" "):
    value = text.partition(before)[2].partition(after)[0].replace(",", "")
    if len(value) == 0:
        numval = 0
    elif "M" in value:
        numval = int(float(value[0:-1]) * 1000000)
    elif "B" in value:
        numval = int(float(value[0:-1]) * 1000000000)
    else:
        numval = int(float(value))
    return numval

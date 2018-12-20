# "minecraft:jump": 173914 -> "jump: 173914"

import json
from io import open

def trim(rawStat):
    dictStat = json.loads(rawStat)
    print(dictStat)
    print(dictStat["nome"])
    for key in dictStat:
        print(key, 'corresponds to', dictStat[key])




if __name__ == "__main__":

    import sys

    if len(sys.argv) == 1:
            print("type help as argument")
    elif len(sys.argv) > 1:
        if sys.argv[1] == 'help':
            print("Usage: $ python trimmer.py <arg1>")
            print("<arg1>: path")
        else:
            # Argomenti passati -----
            path = str(sys.argv[1])
            print("path:", str(path))
            
            with open(path,"r") as f:
                contents = f.read()
                print('Contenuto file:' + contents)
                


# "minecraft:jump": 173914 -> "jump: 173914"

import json
from io import open
import logging


# Configure logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
log.addHandler(streamHandler)


def trim(rawStat):
    '''deleting \"minecraft:\" occurency'''
    
    removeString = "minecraft:"
    newString = ""
    return rawStat.replace(removeString, newString)
    # trimmedString = rawStat.replace(removeString, newString)
    # dictStat = json.loads(trimmedString)
    # print(dictStat)
    # print(dictStat["nome"])

    # for key in dictStat:
    #     print(key, 'corresponds to', dictStat[key])


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
            log.info("Reading file %s", path)

            with open(path, "r") as f:
                contents = f.read()
                log.info("Correctly readed %d characters from file %s", len(contents), path)
                trim(contents)

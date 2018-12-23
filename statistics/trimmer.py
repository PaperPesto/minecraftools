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



if __name__ == "__main__":

    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Return nice and clean Minecraft json statistics')
    parser.add_argument('sourcePath', metavar='sourcePath', type=str, help='the source path of raw json statistics')
    parser.add_argument('targetPath', metavar='targetPath', type=str, help='the target path of clean json statistics')
                        
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                     const=sum, default=max,
    #                     help='sum the integers (default: find the max)')

    args = parser.parse_args()

    sourcePath = args.sourcePath
    targetPath = args.targetPath
    log.info("Reading from file %s", sourcePath)
    log.info("Results will be written to %s", targetPath)
    
    # Read
    try:
        with open(sourcePath, "r") as f:
            contents = f.read()
            log.info("Correctly readed %d characters from file %s", len(contents), sourcePath)
            cleanStats = trim(contents)
    except Exception as e:
        print("exception type:", type(e))
        print("Exception arguments:", e.args)
        print("Exception message:", e)
    
    # Write
    try:
        with open(targetPath, "w") as f:
            contents = f.write(cleanStats)
            log.info("Correctly writed %d characters to file %s", len(cleanStats), targetPath)
    except Exception as e:
        print("exception type:", type(e))
        print("Exception arguments:", e.args)
        print("Exception message:", e)

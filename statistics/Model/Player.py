import logging
import os

# Configure logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
log.addHandler(streamHandler)
# ---

class Player:
    """Minecraft statistics from a player"""
    def __init__(self, path):
        self.path = os.path.abspath(path)
        log.info("absolute path: %s", self.path)
        filename_w_ext = os.path.basename(self.path)
        filename, file_extension = os.path.splitext(filename_w_ext)
        self.uuid = filename
        log.info("uuid: %s", filename)

        self.__readStats()
        

    def __readStats(self):
        """Reads json statistics from file"""
        try:
            with open(self.path, "r") as f:
                self.statistics =  f.read()
                log.info("Correctly readed %d characters from file %s",
                        len(self.statistics), self.path)
        except Exception as e:
            log.error("Errore lettura statistiche: %s", e)


if __name__ == "__main__":
    import sys

    path = sys.argv[1]

    abspath = os.path.abspath(path)

    player = Player(abspath)

    print("abspath", player.path)


    print(player.statistics)

    print("name:", player.uuid)
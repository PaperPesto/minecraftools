import logging
import os

class Player:
    """Minecraft statistics from a player"""

    def __init__(self, path):
        # Configure logging
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.DEBUG)
        streamHandler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        streamHandler.setFormatter(formatter)
        self.log.addHandler(streamHandler)
        # ---

        self.path = path

        filename_w_ext = os.path.basename(self.path)
        self.log.info("basename: %s", filename_w_ext)
        filename, file_extension = os.path.splitext(filename_w_ext)
        self.uuid = filename
        self.log.info("filename: %s", filename)
        



    def readStats(self):

        try:
            with open(self.path, "r") as f:
                self.statistics =  f.read()
                self.log.info("Correctly readed %d characters from file %s",
                        len(self.statistics), self.path)
        except Exception as e:
            self.log.error("Errore lettura statistiche: %s", e)


if __name__ == "__main__":
    import sys

    path = sys.argv[1]

    abspath = os.path.abspath(path)

    player = Player(abspath)

    print("abspath", player.path)

    player.readStats()

    print(player.statistics)

    print("name:", player.uuid)
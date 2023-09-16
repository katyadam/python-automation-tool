import logging
import os

from zipfile import ZipFile

class Unzipper:
    def __init__(self, args: list[str]) -> None:
        self.source: str = args[2]
        self.destination: str = args[3]
        self.log()
    
    def unzip(self) -> None:
        if not os.path.exists(self.destination):
            os.makedirs(self.destination)

        sources = self.source.split(",")
        for src in sources:
            with ZipFile(src, "r") as zipf:
                if os.path.exists(self.destination):
                    zipf.extractall(self.destination)

    def log(self) -> None:
        logging.info("Unzipper created!")
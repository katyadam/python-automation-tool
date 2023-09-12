
import argument_parser
import logging
import os

from td_pairs import TDpair

class Distributor:
    def __init__(self, args: list[str]) -> None:
        self.path: str = args[2]
        self.pair_dataset: dict[str, str] = argument_parser.parse_dataset(args[3])
    
    def distribute(self) -> None:

        for filename in os.listdir(self.path):
            file = os.path.join(self.path, filename)
            new_dest = self.get_file_new_dest(filename)
            if new_dest and os.path.isfile(file):
                subdirectory = os.path.join(self.path, new_dest)
                if not os.path.exists(subdirectory):
                    os.makedirs(subdirectory)
                logging.info(f"File {file} has been succesfully moved to {subdirectory}")
                os.rename(file, os.path.join(subdirectory, filename))


    def get_file_new_dest(self, file: str) -> str:
        file_ext = os.path.splitext(file)[1][1:]
        if file_ext in self.pair_dataset.keys():
            return self.pair_dataset[file_ext]
        else:
            return None


    def log(self) -> None:
        logging.info("Distributor created!")
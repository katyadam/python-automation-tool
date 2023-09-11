
import argument_parser
import logging

from td_pairs import TDpair

class Distributor:
    def __init__(self, args: list[str]) -> None:
        self.path: str = args[2]
        self.pair_dataset: list[TDpair] = argument_parser.parse_dataset(args[3])
    
    def distribute(self) -> None:
        pass

    def log(self) -> None:
        logging.info("Distributor created!")
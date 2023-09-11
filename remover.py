import argument_parser
import os
import logging

from datetime import datetime
from bounds import Bound

class Remover:
    def __init__(self, args: list[str]) -> None:
        self.args: list[str] = args
        self.path: str = args[2]
        self.date: Bound = argument_parser.parse_datetime_bounds(args[3])
        self.types: set[str] = argument_parser.parse_file_types(args[4])
        self.size: Bound = argument_parser.parse_size_bounds(args[5])
    
    def remove(self) -> None:
        for filename in os.listdir(self.path):
            file = os.path.join(self.path, filename)
            if self.can_be_removed(file):
                logging.info(f"File {file} has been succesfully removed!")
                os.remove(file)

    def can_be_removed(self, file: str) -> bool:
        return os.path.isfile(file) and self.check_file_type(file) and self.is_in_daterange(file) and self.is_in_sizerange(file)

    def check_file_type(self, file: str) -> bool:
        file_ext = os.path.splitext(file)[1][1:]
        return file_ext in self.types

    def is_in_daterange(self, file: str) -> bool:
        last_mod_date = datetime.fromtimestamp(os.path.getmtime(file))
        return self.date.lower <= last_mod_date <= self.date.upper
    
    def is_in_sizerange(self, file: str) -> bool:
        file_size = os.path.getsize(file)

        lower_bound = self.size.lower if self.size.lower else 0
        upper_bound = self.size.upper if self.size.upper else float('inf')

        return lower_bound <= file_size <= upper_bound

    def log(self) -> str:
        logging.info("Remover created!")
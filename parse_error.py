import logging

class ParseError(Exception):
    def __init__(self, message: str) -> None:
        logging.error("Please provide date in a valid format: dd.mm.yyyy:hh:mm")
        super().__init__(message)
import logging

class ParseError(Exception):
    def __init__(self, message: str) -> None:
        logging.error("Something unexcepted happened!")
        super().__init__(message)
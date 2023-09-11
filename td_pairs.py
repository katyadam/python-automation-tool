class TDpair:
    """
        Represents pair which consists of Type (pdf, docx, etc...) 
        and directory in which all specified files should be moved 
    """
    def __init__(self, type: str, directory: str) -> None:
        self.type: str = type
        self.directory: str = directory
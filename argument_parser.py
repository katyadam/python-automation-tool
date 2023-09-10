from parse_error import ParseError
from typing import Optional
from datetime import datetime
from bounds import Bound


def parse_size_bounds(size: str) -> Bound:
    """
        Return lower and upper bounds of argument passed size 
    """
    parts = size.split("-")
    if len(parts) != 2:
        return None
    
    lower_bound = int(parts[0]) if parts[0].isdigit() else None
    upper_bound = int(parts[1]) if parts[1].isdigit() else None

    return Bound(lower_bound, upper_bound)

def parse_datetime_bounds(input_range: str) -> Bound:
    """
        Returns tuple of dates representing valid date range or None if error occurs
    """
    parts = input_range.split("-")
    
    if len(parts) != 2:
        return None
    try:
        lower_bound = datetime.strptime(parts[0], "%d.%m.%Y")
        upper_bound = datetime.strptime(parts[1], "%d.%m.%Y")
        return Bound(lower_bound, upper_bound)
    except ValueError:
        raise ParseError("Error occured!")

def parse_file_types(types_arg: str) -> set[str]:
    return set(types_arg.split(","))

    

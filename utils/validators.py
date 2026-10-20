
from dateutil import parser

def parse_date(date_str):
    """
    Try to turn a string into a date object.
    If it fails, raise ValueError.
    """
    try:
        return parser.parse(date_str)
    except Exception:
        raise ValueError("Date format not understood.")

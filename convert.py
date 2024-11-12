from typing import Optional


def str_to_float (a_str:str)-> Optional[float]:
    try:
        return float(a_str)
    except ValueError:
        return None

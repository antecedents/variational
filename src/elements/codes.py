"""Module codes.py"""
import typing


class Codes(typing.NamedTuple):
    """
    The data type class ⇾ Codes<br><br>

    Attributes<br>
    ----------<br>
    <b>board</b> : str
        A health board code<br>

    <b>institution</b> : str
        The code of an institution/hospital

    """

    health_board_code: str
    hospital_code: str

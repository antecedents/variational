"""Module codes.py"""
import pandas as pd

import src.elements.codes as ce


class Codes:
    """
    Determines the unique set of health board & institution pairings
    """

    def __init__(self):
        pass

    @staticmethod
    def __structure(values: list[dict]) -> list[ce.Codes]:
        """

        :param values:
        :return:
        """

        return [ce.Codes(**value) for value in values]

    def exc(self, data: pd.DataFrame) -> list[ce.Codes]:

        frame = data.copy()[['health_board_code', 'hospital_code']].drop_duplicates()
        values: list[dict] = frame.reset_index(drop=True).to_dict(orient='records')

        return self.__structure(values=values)

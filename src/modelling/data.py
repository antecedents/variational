"""Module data.py"""

import pandas as pd


class Data:
    """
    Data
    """

    def __init__(self, data: pd.DataFrame):
        """

        :param data:
        """

        self.__data = data

    def exc(self, hospital_code: int) -> pd.DataFrame:
        """

        :param hospital_code:
        :return:
        """

        return self.__data.loc[self.__data['hospital_code'] == hospital_code, :]

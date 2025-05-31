"""Module persist.py"""
import os

import pandas as pd

import config
import src.elements.codes as ce
import src.elements.inference as ifr
import src.functions.streams


class Persist:
    """
    Constructor
    """

    def __init__(self):
        """
        Constructor
        """

        self.__configurations = config.Config()
        self.__streams = src.functions.streams.Streams()

    def __persist(self, blob: pd.DataFrame, path: str) -> str:
        """

        :param blob:
        :param path:
        :return:
        """

        return self.__streams.write(blob=blob, path=path)

    def exc(self, inference: ifr.Inference, code: ce.Codes) -> str:
        """

        :param inference:
        :param code:
        :return:
        """


        endpoint = os.path.join(
            self.__configurations.assets_, str(code.health_board_code), str(code.hospital_code))

        message = '|'.join((
            str(code.health_board_code),
            str(code.hospital_code),
            self.__persist(blob=inference.evidence_lower_bound, path=os.path.join(endpoint, 'evidence_lower_bound.csv')),
            self.__persist(blob=inference.estimates, path=os.path.join(endpoint, 'estimates.csv'))
        ))

        return message

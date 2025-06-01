"""Module interface.py"""
import logging

import dask
import pandas as pd

import src.elements.master as mr
import src.elements.codes as ce
import src.modelling.data
import src.modelling.split
import src.modelling.architecture
import src.modelling.persist


class Interface:
    """
    <b>Notes</b><br>
    ------<br>
    The interface to drift score programs.<br>
    """

    def __init__(self, data: pd.DataFrame, arguments: dict):
        """

        :param data: The attendances data accident & emergency units
        :param arguments: The arguments.
        """

        self.__data = data
        self.__arguments = arguments



    def exc(self, codes: list[ce.Codes]):
        """

        :param codes:
        :return:
        """

        # Delayed Functions
        __data = dask.delayed(src.modelling.data.Data(data=self.__data).exc)
        __get_splits = dask.delayed(src.modelling.split.Split(arguments=self.__arguments).exc)
        __architecture = dask.delayed(src.modelling.architecture.Architecture(arguments=self.__arguments).exc)
        __persist = dask.delayed(src.modelling.persist.Persist().exc)

        # Compute
        computations = []
        for code in codes:
            data = __data(hospital_code=code.hospital_code)
            master: mr.Master = __get_splits(data=data, code=code)
            inference = __architecture(master=master)
            message = __persist(inference=inference, code=code)
            computations.append(message)
        latest = dask.compute(computations, scheduler='threads')[0]

        logging.info(latest)

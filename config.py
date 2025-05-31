"""
Module config
"""
import datetime
import logging
import os


class Config:
    """
    Class Config

    For project settings
    """

    def __init__(self):
        """
        Constructor
        """

        '''
        Date Stamp: The most recent Tuesday.  The code of Tuesday is 1, hence 
        now.weekday() - 1
        '''
        now = datetime.datetime.now()
        offset = (now.weekday() - 1) % 7
        tuesday = now - datetime.timedelta(days=offset)
        self.stamp: str = tuesday.strftime('%Y-%m-%d')
        logging.info(self.stamp)

        '''
        Keys
        '''
        self.s3_parameters_key = 's3_parameters.yaml'
        self.arguments_key = 'artefacts' + '/' + 'architecture' + '/' + 'variational' + '/' + 'arguments.json'
        self.metadata = 'artefacts/metadata.json'

        '''
        Local Paths
        '''
        sections = ['assets', 'variational', self.stamp]
        self.warehouse: str = os.path.join(os.getcwd(), 'warehouse')
        self.assets_ = os.path.join(self.warehouse, *sections)

        '''
        Cloud
        '''
        self.prefix = '/'.join(sections)

        '''
        Extra
        '''
        self.fields = ['week_ending_date', 'health_board_code', 'hospital_code', 'n_attendances']

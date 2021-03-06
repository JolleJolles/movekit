"""
  CSV I/O in Python.
  Load the csv data into pandas dataframe.
  Author: Arjun Majumdar, Eren Cakmak
  Created: July, 2019
"""

import pandas as pd
from pandas.api.types import is_numeric_dtype, is_string_dtype
from pandas.io.common import EmptyDataError


def parse_csv(path_to_file):
    '''
    A function to read CSV file into a Pandas DataFrame-
    Expects complete path/relative path to CSV file along with file name
    '''
    try:

        if path_to_file[-3:] == 'csv':
            data = pd.read_csv(path_to_file)
        else:
            data = pd.read_csv(path_to_file + '.csv')

        # change column names all to lower case values
        data.columns = map(str.lower, data.columns)

        # check if all required columns are there in the right format
        if 'time' in data and 'animal_id' in data and 'x' in data and 'y' in data:
            # Check if 'time' attribute is integer-
            if is_numeric_dtype(data['time']):
                data.sort_values('time', ascending=True, inplace=True)
                # Check if 'time' attribute is string-
            elif is_string_dtype(data['time']):
                data['time'] = pd.to_datetime(data['time'])
                data.sort_values('time', ascending=True, inplace=True)

            return data
    except FileNotFoundError:
        print(
            "Your file below could not be found.\nPath given: {0}\n\n".format(
                path_to_file))
    except EmptyDataError:
        print(
            'Your file is empty, has no header, or misses some required columns.'
        )

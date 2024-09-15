import os
from importlib import import_module, resources
from typing import Union

DATA_DIR = os.path.join(resources.files(__package__), "data")
DEFAULT_FRAMEWORK = os.environ.get('DATAFRAME_FRAMEWORK', 'pandas').lower()

def _dataframe_module():
    """Dynamically import and return the appropriate dataframe module."""
    if DEFAULT_FRAMEWORK == 'pandas':
        return import_module('pandas')
    elif DEFAULT_FRAMEWORK == 'polars':
        return import_module('polars')
    else:
        raise ValueError("BABYNAMES_FRAMEWORK must be either 'pandas' or 'polars'")

def _load_dataframe(file_path: str) -> Union['pandas.DataFrame', 'polars.DataFrame']:
    """Load a dataframe using the specified dataframe framework."""
    df_module = _dataframe_module()
    return df_module.read_csv(file_path)

# Load dataframes on import
babynames = _load_dataframe(os.path.join(DATA_DIR, 'babynames.csv.zip'))
applicants = _load_dataframe(os.path.join(DATA_DIR, 'applicants.csv'))
births = _load_dataframe(os.path.join(DATA_DIR, 'births.csv'))
lifetables = _load_dataframe(os.path.join(DATA_DIR, 'lifetables.csv'))

# Attach help documentation to the object
babynames.__doc__ = """
Babynames Dataset

This dataset contains information about baby names in the United States.

Columns:
- year: The year of the record (integer)
- name: The given name (string)
- sex: The sex associated with the name (string, 'F' for female or 'M' for male)
- number: The number of babies given this name in this year (integer)
"""

applicants.__doc__ = """
Applicants Dataset

This dataset contains information about Social Security Number applicants.

Columns:
- year: The year of the record (integer)
- sex: The sex of the applicants (string, 'F' for female or 'M' for male)
- n_all: The number of applicants in this year and sex category (integer)
"""

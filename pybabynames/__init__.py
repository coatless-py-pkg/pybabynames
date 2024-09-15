import os
from importlib import import_module
from importlib_resources import files
from typing import Union

DATA_DIR = os.path.join(files(__package__), 'data')
DEFAULT_FRAMEWORK = os.environ.get('DATAFRAME_FRAMEWORK', 'polars').lower()

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
    return df_module.read_parquet(file_path)

# Load dataframes on import
babynames = _load_dataframe(os.path.join(DATA_DIR, 'babynames.parquet'))
applicants = _load_dataframe(os.path.join(DATA_DIR, 'applicants.parquet'))
births = _load_dataframe(os.path.join(DATA_DIR, 'births.parquet'))
lifetables = _load_dataframe(os.path.join(DATA_DIR, 'lifetables.parquet'))

# Attach help documentation to the object
babynames.__doc__ = """
Babynames Dataset

This dataset contains information about baby names in the United States.

Columns:
- year: The year of the record (integer)
- sex: The sex associated with the name (string, 'F' for female or 'M' for male)
- name: The given name (string)
- n: The number of babies given this name in this year (integer)
- prop: The proportion of babies given this name in this year (float)
"""

applicants.__doc__ = """
Applicants Dataset

This dataset contains information about Social Security Number applicants.

Columns:
- year: The year of the record (integer)
- sex: The sex of the applicants (string, 'F' for female or 'M' for male)
- n_all: The number of applicants in this year and sex category (integer)
"""

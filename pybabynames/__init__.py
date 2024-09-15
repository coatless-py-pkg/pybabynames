import os
import warnings
from importlib import import_module
from importlib_resources import files
from typing import Union

# Define the data directory
DATA_DIR = os.path.join(files(__package__), 'data')

# Define valid framework options
FrameworkType = Literal['pandas', 'polars']
VALID_FRAMEWORKS: list[FrameworkType] = ['pandas', 'polars']

# Set the default dataframe framework
DEFAULT_FRAMEWORK: FrameworkType = 'polars'

def _dataframe_framework() -> FrameworkType:
    """
    Get the dataframe framework from the environment variable or use the default.

    Returns:
        FrameworkType: The selected dataframe framework.
    """
    framework = os.environ.get('DATAFRAME_FRAMEWORK', DEFAULT_FRAMEWORK).lower()
    if framework not in VALID_FRAMEWORKS:
        warnings.warn(f"Invalid DATAFRAME_FRAMEWORK '{framework}'. Using default: {DEFAULT_FRAMEWORK}", RuntimeWarning)
        return DEFAULT_FRAMEWORK
    return framework

CURRENT_FRAMEWORK = get_dataframe_framework()

def _dataframe_module():
    """
    Dynamically import and return the appropriate dataframe module.

    Returns:
        module: The imported dataframe module (either pandas or polars).
    """
    return import_module(CURRENT_FRAMEWORK)

def _load_dataframe(file_path: str) -> Union['pandas.DataFrame', 'polars.DataFrame']:
    """
    Load a dataframe using the specified dataframe framework.

    Args:
        file_path (str): The path to the Parquet file to be loaded.

    Returns:
        Union['pandas.DataFrame', 'polars.DataFrame']: The loaded dataframe.
    """
    df_module = _dataframe_module()
    return df_module.read_parquet(file_path)

# Attempt to load dataframes on import
try:
    babynames = _load_dataframe(os.path.join(DATA_DIR, 'babynames.parquet'))
    applicants = _load_dataframe(os.path.join(DATA_DIR, 'applicants.parquet'))
    births = _load_dataframe(os.path.join(DATA_DIR, 'births.parquet'))
    lifetables = _load_dataframe(os.path.join(DATA_DIR, 'lifetables.parquet'))
except:
    warnings.warn(f"Failed to load dataframes!", RuntimeWarning)
    babynames = applicants = lifetables = births = None

# Attach help documentation to the object
babynames.__doc__ = """
Baby names.

Full baby name data provided by the SSA. This includes all names with at least 5 uses.

Columns:
    year (int): The year of the record.
    sex (str): The sex associated with the name ('F' for female or 'M' for male).
    name (str): The given name.
    n (int): The number of applicants with this name.
    prop (float): The proportion of applicants with this name (n divided by total number
        of applicants in that year, which means proportions are of people of
        that sex with that name born in that year).
"""

applicants.__doc__ = """
Applicants.

The SSA baby names data comes from social security number (SSN) applications.
SSA cards were first issued in 1936, but were only needed for people with
an income. In 1986, the law changed effectively requiring all children to
get an SSN at birth.

Columns:
    year (int): The year of the record.
    sex (str): The sex of the applicants.
    applicants (int): The number of applicants.
"""


births.__doc__ = """
Births

Live births data from census.gov.

Columns:
    year (int): Year.
    births (int): Number of live births, rounded to nearest 1000.
"""

lifetables.__doc__ = """
Lifetables

Cohort life tables data as provided by SSA.

Columns:
    x (int): Age in years.
    qx (float): Probability of death at age x.
    lx (int): Number of survivors, of birth cohort of 100,000, at next integral age.
    dx (int): Number of deaths that would occur between integral ages.
    Lx (float): Number of person-years lived between x and x+1.
    Tx (float): Total number of person-years lived beyond age x.
    ex (float): Average number of years of life remaining for members of cohort alive at age x.
    sex (str): Sex.
    year (int): Year.

For further details, see http://www.ssa.gov/oact/NOTES/as120/LifeTables_Body.html#wp1168594
"""

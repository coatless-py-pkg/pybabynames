# pybabynames

[![PyPI](https://img.shields.io/pypi/v/pybabynames.svg)](https://pypi.org/project/pybabynames/)
[![Tests](https://github.com/coatless-py-pkg/pybabynames/actions/workflows/test.yml/badge.svg)](https://github.com/coatless-py-pkg/pybabynames/actions/workflows/test.yml)
[![Changelog](https://img.shields.io/github/v/release/coatless-py-pkg/pybabynames?include_prereleases&label=changelog)](https://github.com/coatless-py-pkg/pybabynames/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/coatless-py-pkg/pybabynames/blob/main/LICENSE)

Python port of the R data package 'babynames'. This package provides US baby names data from the Social Security Administration (SSA). It contains all names used for at least 5 children of either sex in the United States. The package features the ability to switch between the data being imported as a Pandas DataFrame or a Polars DataFrame by setting an environment variable.

## Installation

Install this library using `pip`:

```bash
pip install pybabynames
```

## Usage


```python
import pybabynames as bn

# Retrieve DataFrame of baby names
babynames = bn.babynames

# Retrieve DataFrame of applicant data for SSN
applicants = bn.applicants

# Retrieve DataFrame of Birth Data
births = bn.births

# Retrieve DataFrame of life expectancy
lifetables = bn.lifetables
```

> [!IMPORTANT]
>
> By default, we'll attempt to use the `polars` module. You can switch back to using `pandas` by
> specifying before `babynames` import statement an environment flag like so:
>
> ```python
> import os
> os.environ["DATAFRAME_FRAMEWORK"] = "pandas"
> ```

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

```bash
cd pybabynames
python -m venv venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:

```bash
python -m pip install -e '.[test]'
```

To run the tests:

```bash
python -m pytest
```

## Acknowledgement

This Python package is a port of the R Data package `babynames` by Hadley Wickham.

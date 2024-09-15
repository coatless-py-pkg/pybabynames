from setuptools import setup, find_packages

setup(
    name='babynames',
    version='0.1',
    packages=find_packages(),
    package_data={'babynames': ['data/*.csv.*']},
    install_requires=[],  # No hard requirements
    extras_require={
        'pandas': ['pandas'],
        'polars': ['polars'],
    },
)

from setuptools import setup, find_packages

setup(
    name='pybabynames',
    version='0.1',
    packages=find_packages(),
    package_data={'pybabynames': ['data/*.csv.*']},
    install_requires=["importlib-resources"],
    extras_require={
        'pandas': ['pandas'],
        'polars': ['polars'],
    },
)

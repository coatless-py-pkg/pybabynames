import os
import pytest
import pybabynames as bn

@pytest.fixture(scope="module")
def env_setup():
    """Set up the environment variable for testing."""
    original = os.environ.get('DATAFRAME_FRAMEWORK')
    os.environ['DATAFRAME_FRAMEWORK'] = 'polars'
    yield
    if original is None:
        del os.environ['DATAFRAME_FRAMEWORK']
    else:
        os.environ['DATAFRAME_FRAMEWORK'] = original

@pytest.mark.parametrize("dataset", ['babynames', 'applicants', 'lifetables', 'births'])
def test_dataframes_loaded(env_setup, dataset):
    """Test that all dataframes are properly loaded."""
    df = getattr(bn, dataset)
    assert df is not None
    assert len(df) > 0
    assert hasattr(df, '__doc__')
    assert df.__doc__ is not None

@pytest.mark.parametrize("dataset, expected_columns", [
    ('babynames', ['year', 'sex', 'name', 'n', 'prop']),
    ('applicants', ['year', 'sex', 'n_all']),
    ('lifetables', ['x', 'qx', 'lx', 'dx', 'Lx', 'Tx', 'ex', 'sex', 'year']),
    ('births', ['year', 'births'])
])
def test_dataframe_columns(dataset, expected_columns):
    """Test that dataframes have the expected columns."""
    df = getattr(bn, dataset)
    assert list(df.columns) == expected_columns

@pytest.mark.parametrize("dataset, expected_text", [
    ('babynames', "Baby names"),
    ('applicants', "Applicants"),
    ('births', "Births"),
    ('lifetables', "Lifetables")
])
def test_documentation(dataset, expected_text):
    """Test that documentation is accessible and contains expected text."""
    df = getattr(bn, dataset)
    assert df.__doc__ is not None, f"{dataset} should have a docstring"
    assert expected_text in df.__doc__, f"{dataset} docstring should contain '{expected_text}'"

@pytest.mark.parametrize("framework", ['pandas', 'polars'])
def test_different_frameworks(framework):
    """Test that the package works with different frameworks."""
    os.environ['DATAFRAME_FRAMEWORK'] = framework
    import importlib
    importlib.reload(bn)
    for dataset in ['babynames', 'applicants', 'lifetables', 'births']:
        assert hasattr(bn, dataset)
        df = getattr(bn, dataset)
        assert len(df) > 0

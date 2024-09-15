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

def test_dataframes_loaded(env_setup):
    """Test that dataframes are properly loaded."""
    assert hasattr(bn, 'babynames')
    assert hasattr(bn, 'applicants')
    assert len(bn.babynames) > 0
    assert len(bn.applicants) > 0

def test_dataframe_columns():
    """Test that dataframes have the expected columns."""
    expected_babynames_columns = ['year', 'sex', 'name', 'n', 'prop']
    expected_applicants_columns = ['year', 'sex', 'n_all']
    assert list(bn.babynames.columns) == expected_bn_columns
    assert list(bn.applicants.columns) == expected_applicants_columns

def test_documentation():
    """Test that documentation is accessible."""
    assert bn.babynames.__doc__ is not None
    assert bn.applicants.__doc__ is not None
    assert "bn Dataset" in bn.babynames.__doc__
    assert "Applicants Dataset" in bn.applicants.__doc__

@pytest.mark.parametrize("framework", ['pandas', 'polars'])
def test_different_frameworks(framework):
    """Test that the package works with different frameworks."""
    os.environ['DATAFRAME_FRAMEWORK'] = framework
    import importlib
    importlib.reload(bn)
    assert hasattr(bn, 'bn')
    assert hasattr(bn, 'applicants')

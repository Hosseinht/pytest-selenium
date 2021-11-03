import pytest


def test_example():
    print('test1')
    assert 1 == 1


@pytest.mark.slow
def test_example1():
    assert 1 == 1

# pytest -x: stopping after 1 failure
# pytest -rP: output print statement
# pytest core: specify a test folder ==> pytest tests/test_ex1.py::test_example
# pytest mark. @pytest.mark.skip : skip a test
# pytest mark. @pytest.mark.xfail : a test that we know it's going to fail
# make our own marker ==> pytest.ini
# pytest -m "slow": just the tests that have been marked as slow are going to run

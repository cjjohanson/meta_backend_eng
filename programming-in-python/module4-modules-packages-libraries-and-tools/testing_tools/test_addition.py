import pytest
import addition

def test_add():
    assert addition.add(4, 5) == 9


def test_subtract():
    assert addition.sub(4, 5) == -1


# Use python -m pytest test_addition.py to run the tests
# and see the outputs
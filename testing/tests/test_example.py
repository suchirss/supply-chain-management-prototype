import pytest

from test_functions import add

def test_add_numbers():
    test_data = ((1, 2), 3) # Arrange
    result = add(test_data[0][0], test_data[0][1])
    assert result == test_data[1]
import pytest
from calculator import calculate_average


def test_calculate_average_with_valid_scores():
    assert calculate_average([80, 90, 100]) == 90


def test_calculate_average_with_single_score():
    assert calculate_average([75]) == 75


def test_calculate_average_with_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])
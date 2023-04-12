import pytest
from my_test_lambda.handler_my_func import split_numbers, get_two_numbers


@pytest.mark.parametrize("size_len, size_expected",
                         [
                             (6, 120),
                             (5, 60),
                             (9, 504)
                         ]
                         )
def test_split_numbers(size_len, size_expected):
    numbers = split_numbers(size_len)

    assert len(numbers) == size_expected


@pytest.mark.parametrize("number, results",
                         [
                             (130321, [[130, 231], [131, 230]]),
                         ])
def test_get_two_numbers(number, results):
    data = get_two_numbers(number)

    assert data == results

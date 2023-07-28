import pytest


def sum_to_num(a, b):
    return a + b


def test_sum():
    assert sum_to_num(2, 3) == 5, 'Ошибка'


if __name__ == '__main__':
    pytest.main()

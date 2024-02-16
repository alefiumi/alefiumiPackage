# tests/test_count.py

from ft_package.count import count_in_list


def test_count_in_list():
    lst = [1, 2, 3, 4, 4, 5]
    assert count_in_list(lst, 4) == 2

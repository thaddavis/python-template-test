from basic_math import BasicMath


def test_add():
    """
    testing 3 + 2 = 5
    """
    assert BasicMath.add(3, 2) == 5


def test_subtract():
    assert BasicMath.subtract(3, 2) == 1

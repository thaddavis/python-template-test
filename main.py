
from modules.basic_math import BasicMath

print("Hello World!")

assert BasicMath.add(1, 3) == 4, "1 + 3 should equal 4"
assert BasicMath.subtract(1, 3) == -2, "1 - 3 should equal -2"


def test_answer():
    assert BasicMath.add(3, 2) == 5

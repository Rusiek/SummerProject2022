# Krzysztof Wysocki
import pytest
from ....readstdout import checkstdout
from .prog import f as user_sol
from .sol import f as corr_sol
from random import randint

MIN_RANGEE = 10 ** 1500
MAX_RANGE = 10 ** 20000
AMOUNT = 10
TESTS = [randint(MIN_RANGEE, MAX_RANGE) for i in range(AMOUNT)]


@pytest.mark.order(3)
@pytest.mark.parametrize("data", TESTS)
def test_basic(data):
    assert checkstdout(user_sol, corr_sol, [data])

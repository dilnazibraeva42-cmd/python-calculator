from src.advanced import power, percent


def test_power():
    assert power(2, 3) == 8


def test_percent():
    assert percent(200, 10) == 20

from bank import value


def test_value_zero():
    assert value("Hello sir") == int(0)


def test_value_twenty():
    assert value("hi, sir") == int(20)


def test_value_hundred():
    assert value("whats up") == int(100)

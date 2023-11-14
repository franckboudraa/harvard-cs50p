from fuel import convert, gauge
from pytest import raises

def test_convert():
    with raises(ZeroDivisionError):
        assert convert("1/0")

    with raises(ValueError):
        assert convert("6/5")

    assert convert("5/6") == 83

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(83) == "83%"
    assert gauge(1) == "E"

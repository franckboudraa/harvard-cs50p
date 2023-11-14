import pytest
from working import convert


def test_convert_bad_1():
    with pytest.raises(ValueError):
        convert("")


def test_convert_bad_2():
    with pytest.raises(ValueError):
        convert("hi")


def test_convert_bad_3():
    with pytest.raises(ValueError):
        convert("12:00 to 13:00")


def test_convert_bad_4():
    with pytest.raises(ValueError):
        convert("1 to 2")


def test_convert_bad_5():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")


def test_convert_good_1():
    assert(convert("9:00 AM to 5:00 PM") == "09:00 to 17:00")


def test_convert_good_2():
    assert(convert("9 AM to 5 PM") == "09:00 to 17:00")


def test_convert_good_3():
    assert(convert("9:30 AM to 5 PM") == "09:30 to 17:00")


def test_convert_good_4():
    assert(convert("12:30 AM to 1:59 PM") == "00:30 to 13:59")

from twttr import shorten


def test_shorten():
    assert shorten("Bonjour") == "Bnjr"
    assert shorten("OO") == ""
    assert shorten("BCD") == "BCD"
    assert shorten("1 test") == "1 tst"
    assert shorten("1, 2, 3") == "1, 2, 3"

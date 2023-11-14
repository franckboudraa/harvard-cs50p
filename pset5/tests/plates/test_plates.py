from plates import is_valid


def test_is_valid_len():
    assert is_valid("A") == False


def test_is_valid_num_middle():
    assert is_valid("AAA22A") == False


def test_is_valid_zero():
    assert is_valid("AAA022") == False


def test_is_valid_punct():
    assert is_valid("AA!") == False


def test_is_valid_beg_alpha():
    assert is_valid("222AAA") == False


def test_is_valid_right():
    assert is_valid("AAA222") == True


def test_is_valid_begin_bis():
    assert is_valid("A2") == False

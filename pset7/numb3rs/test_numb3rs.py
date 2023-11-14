from numb3rs import validate

def test_validate_bad_1():
    assert(validate("") == False)

def test_validate_bad_2():
    assert(validate("275.3.6.28") == False)

def test_validate_bad_3():
    assert(validate("1..3.4") == False)

def test_validate_bad_4():
    assert(validate("255.566.553.554") == False)

def test_validate_good_1():
    assert(validate("1.1.1.1"))

def test_validate_good_2():
    assert(validate("255.255.255.255"))

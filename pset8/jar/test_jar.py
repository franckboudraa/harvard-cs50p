from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError) as res:
        jar = Jar(-1)
        assert res.type == ValueError

    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()

    with pytest.raises(ValueError) as res:
        jar.deposit(-1)
        assert res.type == ValueError

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_withdraw():
    jar = Jar()

    with pytest.raises(ValueError) as res:
        jar.withdraw(-1)
        assert res.type == ValueError

    jar.deposit(3)
    jar.withdraw(1)
    assert str(jar) == "🍪🍪"

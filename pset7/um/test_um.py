from um import count

def test_um_1():
    assert(count("") == 0)

def test_um_2():
    assert(count("um") == 1)


def test_um_3():
    assert(count("hum") == 0)


def test_um_4():
    assert(count("umum") == 0)


def test_um_5():
    assert(count("once upon a um!") == 1)


def test_um_6():
    assert(count("yummy") == 0)


def test_um_7():
    assert(count("um um um") == 3)


def test_um_8():
    assert(count("um, um, um") == 3)


def test_um_9():
    assert(count("Hello, Um, World!") == 1)

import pytest
from seasons import convert

def test_convert_bad_input():
    with pytest.raises(SystemExit) as res:
        convert("Hello, world!")
        assert res.type == SystemExit
        assert res.value == "Invalid date"


def test_convert_good_input():
    assert(convert("1970-01-01") == "Twenty-eight million, three hundred twenty-three thousand, three hundred sixty minutes")

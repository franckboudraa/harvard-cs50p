import pytest
from Weather import Weather


def test_weather_city():
    weather = Weather("Paris")
    assert weather.city == "Paris"

    weather.city = "London"
    assert weather.city == "London"


def test_weather_date_good():
    weather = Weather()
    assert weather.date == "today"

    weather.date = "tomorrow"
    assert weather.date == "tomorrow"


def test_weather_date_bad():
    with pytest.raises(ValueError):
        assert Weather(date="yesterday")


def test_weather_unit_group_good():
    weather = Weather()
    assert weather.unit_group == "metric"

    weather.unit_group = "us"
    assert weather.unit_group == "us"


def test_weather_unit_group_bad():
    with pytest.raises(ValueError):
        assert Weather(unit_group="kos")


def test_get_emoji_for_condition_good():
    weather = Weather()
    assert weather.get_emoji_for_condition("clear-day") == "☀️"


def test_get_emoji_for_condition_bad():
    weather = Weather()
    assert weather.get_emoji_for_condition("we don't know") == "❔"

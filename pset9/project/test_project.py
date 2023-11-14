from pytest import raises
from Weather import Weather
from io import StringIO
from project import (
    main,
    prompt_for_city,
    display_progress_bar,
    display_forecast,
    clear_screen,
    footer_actions,
)


def test_main(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", StringIO("Paris"))

    with raises(EOFError):  # program end
        main()
        captured = capsys.readouterr()

        assert captured.out == "For which city do you want weather ? "


def test_prompt_for_city(monkeypatch):
    # monkeypatch the "input" function, so that it returns "Paris".
    # This simulates the user entering "Paris" in the terminal:
    monkeypatch.setattr("sys.stdin", StringIO("Paris"))

    assert prompt_for_city() == "Paris"


def test_display_progress_bar(capsys):
    display_progress_bar("London")
    captured = capsys.readouterr()

    assert "Loading weather forecast for London" in captured.out


def test_display_forecast(monkeypatch, capsys):
    with raises(SystemExit) as exit_info:  # program end
        monkeypatch.setattr("sys.stdin", StringIO("q"))

        weather = Weather(city="London")
        display_forecast(weather)
        captured = capsys.readouterr()

        assert "Weather forecast for London" in captured.out
        assert exit_info.value.code == 0


def test_clear_screen():
    assert clear_screen() == None


def test_footer_actions(monkeypatch, capsys):
    with raises(SystemExit) as exit_info:  # program end
        monkeypatch.setattr("sys.stdin", StringIO("q"))

        weather = Weather(city="San Francisco")
        footer_actions(weather)
        captured = capsys.readouterr()

        assert "t: tomorrow forecast" in captured.out
        assert exit_info.value.code == 0

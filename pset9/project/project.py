import os
import time
import sys
from rich import print
from rich.progress import track
from Weather import Weather


# Using a class would have be a better design choice here
# but it was required to have at least 3 inline functions:
#
# > "Your 3 required custom functions other than main must also
# > be in project.py and defined at the same indentation level
# > as main (i.e., not nested under any classes or functions)."


def main(weather=Weather()):
    """
    Main screen
    We pass an optional weather argument to be able to restart the program
    and change city without losing other params
    """

    clear_screen()
    user_input = prompt_for_city()

    weather.city = user_input

    display_progress_bar(weather.city)
    display_forecast(weather)

    return True


def prompt_for_city() -> str:
    """Prompt user to enter a city, which will be used to fetch weather forecast"""
    return input("For which city do you want weather ? ").strip()


def display_progress_bar(city) -> None:
    """Display progress bar while fetching weather forecast"""
    for _ in track(
        range(80),
        description=f"Loading weather forecast for [bold cyan]{city}[/bold cyan]",
    ):
        time.sleep(0.01)


def display_forecast(weather) -> None:
    """Display weather forecast + footer actions"""
    clear_screen()
    weather.display_forecast()
    footer_actions(weather)


def clear_screen() -> None:
    """Clear terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def footer_actions(weather: Weather) -> None:
    """
    Display a menu of actions at the bottom of the screen
    to offer user the ability to change city, units or date of forecast
    """

    print(
        f"[bold]t[/bold]: {'today' if weather.date == 'tomorrow' else 'tomorrow'} forecast",
        end=" | ",
    )
    print("[bold]c[/bold]: change city", end=" | ")

    if weather.unit_group != "metric":
        print("[bold]e[/bold]: metric units (C°, km)", end=" | ")

    if weather.unit_group != "us":
        print("[bold]s[/bold]: US units (F°, miles)", end=" | ")

    if weather.unit_group != "uk":
        print("[bold]k[/bold]: UK units (C°, miles)", end=" | ")

    print("[bold]q[/bold]: exit")

    user_input = input().strip().lower()

    match user_input:
        case "t":
            if weather.date == "today":
                weather.date = "tomorrow"
            else:
                weather.date = "today"

            display_forecast(weather)
        case "c":
            main(weather)
        case "e":
            weather.unit_group = "metric"
            display_forecast(weather)
        case "s":
            weather.unit_group = "us"
            display_forecast(weather)
        case "k":
            weather.unit_group = "uk"
            display_forecast(weather)
        case "q":
            sys.exit(0)
        case _:
            sys.exit("Invalid input provided")


if __name__ == "__main__":
    main()

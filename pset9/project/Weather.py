import requests
from rich import print

API_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices"
API_KEY = "G346D5HB6NZXYCM5HHV9SYLYM"


class Weather:
    def __init__(
        self, city: str = "", date: str = "today", unit_group: str = "metric"
    ) -> None:
        self.city = city
        self.date = date
        self.unit_group = unit_group

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, city: str) -> None:
        self._city = city

    @property
    def date(self) -> str:
        return self._date

    @date.setter
    def date(self, date: str) -> None:
        if date not in ["today", "tomorrow"]:
            raise ValueError("Invalid date provided")
        else:
            self._date = date

    @property
    def unit_group(self) -> str:
        return self._unit_group

    @unit_group.setter
    def unit_group(self, unit_group: str) -> None:
        if unit_group not in ["metric", "us", "uk"]:
            raise ValueError("Invalid unit group provided")
        else:
            self._unit_group = unit_group

    def get_forecast(self) -> dict:
        """Fetch weather forecast"""
        payload = {
            "unitGroup": self.unit_group,
            "key": API_KEY,
            "contentType": "json",
        }
        req = requests.get(
            f"{API_URL}/rest/services/timeline/{self.city}/{self.date}",
            params=payload,
            timeout=5,
        )

        return req.json()

    def display_forecast(self) -> None:
        """Display forecast for city"""
        forecast = self.get_forecast()

        if forecast["resolvedAddress"]:
            print(
                f"Weather forecast for [bold cyan]{forecast['resolvedAddress']}[/bold cyan]"
            )

            print()

            if self.date == "today":
                print("[bold]Current conditions[/bold]")
                print(
                    f"{self.get_emoji_for_condition(forecast['currentConditions']['icon'])} [bold]{forecast['currentConditions']['conditions']}[/bold]"
                )
                print(
                    f"Bulletin of {forecast['currentConditions']['datetime']} (local time)"
                )
                print(
                    f"Temperature is {forecast['currentConditions']['temp']} °{self.get_temperature_unit()}",
                    end=", ",
                )
                print(
                    f"while perceived temperature is {forecast['currentConditions']['feelslike']} °{self.get_temperature_unit()}"
                )
                print(f"Humidity: {int(forecast['currentConditions']['humidity'])} %")
                print(
                    f"Precipitations probability: {int(forecast['currentConditions']['precipprob'])} %"
                )
                print(
                    f"Wind speed: {forecast['currentConditions']['windspeed']} {self.get_distance_unit()}/h"
                )
                print(f"UV index: {int(forecast['currentConditions']['uvindex'])}")
                print()
            print(f"[bold]{self.date.title()} forecast[/bold]")
            print(
                f"{self.get_emoji_for_condition(forecast['days'][0]['icon'])}  [bold]{forecast['days'][0]['conditions']}[/bold]"
            )
            print(f"[italic]{forecast['days'][0]['description']}[/italic]")
            print(
                f"Minimum temperature: {forecast['days'][0]['tempmin']} °{self.get_temperature_unit()}"
            )
            print(
                f"Maximum temperature: {forecast['days'][0]['tempmax']} °{self.get_temperature_unit()}"
            )
            print(
                f"Precipitations probability: {int(forecast['days'][0]['precipprob'])} %"
            )
            print(
                f"Wind speed: {forecast['days'][0]['windspeed']} {self.get_distance_unit()}/h"
            )
            print(f"UV index: {int(forecast['days'][0]['uvindex'])}")
            print(f"Sunrise: {forecast['days'][0]['sunrise']}")
            print(f"Sunset: {forecast['days'][0]['sunset']}")
            print()

            if self.date == "today":
                print("[bold]Next days forecast[/bold]")
                print(f"[italic]{forecast['description']}[/italic]")
                print()
        else:
            print("No city or forecast are available based on your input")

    def get_emoji_for_condition(self, condition: str) -> str:
        """Return emoji for weather condition"""
        match condition:
            case "snow":
                return "🌨️"
            case "rain":
                return "🌧️"
            case "fog":
                return "🌫️"
            case "wind":
                return "💨"
            case "cloudy":
                return "☁️"
            case "partly-cloudy-day":
                return "⛅"
            case "partly-cloudy-night":
                return "☁️"
            case "clear-day":
                return "☀️"
            case "clear-night":
                return "🌙"
            case _:
                return "❔"

    def get_distance_unit(self) -> str:
        """Return distance unit based on selected variation"""
        if self.unit_group == "metric":
            return "km"
        else:
            return "miles"

    def get_temperature_unit(self) -> str:
        """Return temperature unit based on selected variation"""
        if self.unit_group == "metric" or self.unit_group == "uk":
            return "C"  # Celsius
        else:
            return "F"  # Fahrenheit

# Weather in terminal
By Franck Boudraa - Rennes (France)

### Video Demo
https://youtu.be/Sq0JADw4c4U

### Description
The "Weather in terminal" program lets you consult the weather forecast for the city of your choice, for today, tomorrow or the next few days.

You can change the city while the program is running, as well as temperature units (celsius or fahrenheit) and distance units (kilometers/hour or miles/hour) to suit everyone.

It was a fun program to write for the CS50 Python course!

### Design
I use the free Visual Crossing API (visualcrossing.com) to fetch weather.

Using a class would have be a better design choice on project.py but it was required to have at least 3 inline functions :
> Your 3 required custom functions other than main must also
> be in project.py and defined at the same indentation level
> as main (i.e., not nested under any classes or functions).


### Requirements
Libraries used from PyPI (use pip to install those libraries):
- pytest (for testing)
- requests (for making API requests)
- rich (for rendering better styles on terminal)

If the program doesn't work and you have an error from Visual Crossing API, perhaps you need to update the Visual Crossing API key on Weather.py (var "API_KEY"). If so, you need to register on visualcrossing.com to get a free API key.

### Start program

```
python project.py
```
The program will ask you to enter the name of a city for which to retrieve the weather.

### Options
While the program is running, once you've entered the name of a city and retrieved the weather forecast, you can perform certain actions:

- ```t``` to change between today and tomorrow forecast
- ```s``` to switch on US units (°F and miles)
- ```k``` to switch on UK units (°C and miles)
- ```e``` to switch on european units (°C and kilometers)
- ```q``` to exit the program

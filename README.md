# Weather Application

This is a Python-based desktop weather application that provides real-time weather data for any city in the world using the OpenWeatherMap API. It uses the Tkinter library for the GUI.

## Dependencies
* Python 3.x
* tkinter
* configparser
* requests

## Installation

Clone the repository:
```
git clone https://github.com/Kofenzz/Weather_APP_with_GUI.git
```

Install the dependencies using pip:
```
pip install tkinter configparser requests
```

## Usage

1. Navigate to the cloned repository directory
2. Open the `config.ini` file and insert your OpenWeatherMap API key
3. Run the application using the following command:
```
python main.py
```
4. Type in the name of the city you want to get weather data for in the input field and click the "Search Weather" button.

The application will display the following weather data for the entered city:
* Location (city and country)
* Temperature in Celsius and Fahrenheit
* Weather condition
* Weather icon

If the entered city cannot be found, an error message will be displayed.

## Credits

This application was created by Kofenzz. It uses the OpenWeatherMap API to get real-time weather data.

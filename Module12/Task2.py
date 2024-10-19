import requests
api_key = "b89a4fe41107b250a54812e5e2814166"

class Inputs:
    def __init__(self, city_name, state_code, country_code):
        self.city_name = city_name
        self.state_code = state_code
        self.country_code = country_code
        self.validate_inputs()

    def validate_inputs(self):
        inputs = {
            "city_name": self.city_name,
            "state_code": self.state_code,
            "country_code": self.country_code
        }

        for key, value in inputs.items():
            if len(value) < 2:
                print(f"Invalid input. {value} must have at least 2 characters. ")

    def req(self):
        coordinate_request = f"http://api.openweathermap.org/geo/1.0/direct?q={self.city_name},{self.state_code},{self.country_code}&appid={api_key}"

        coordinate_response = requests.get(coordinate_request)
        json_format = coordinate_response.json()
        lat = json_format[0]["lat"]
        lon = json_format[0]["lon"]

        weather_request = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
        weather_response = requests.get(weather_request)
        json_format_weather = weather_response.json()
        l = []
        l.append(json_format_weather)

        main = l[0]["main"]
        temp = main["temp"]
        feels_like = main["feels_like"]
        temp_min = main["temp_min"]
        temp_max = main["temp_max"]
        humidity = main["humidity"]

        main_desc = l[0]["weather"]
        status = main_desc[0]["main"]
        description = main_desc[0]["description"]

        formula = 273.15  # To convert to celsius from Klein

        output = f"Temperature: {round(temp - formula)} | Feels Like: {round(feels_like - formula)} | Minimum Temperature: {round(temp_min - formula)} | Maximum Temperature: {round(temp_max - formula)} | Humidity: {humidity}% | Status: {status} | Description: {description}"
        print(output)

# Main program

# initializer = Inputs(input("Enter a city name: "), input("Enter a state code: "), input("Enter a country code: "))
initializer = Inputs("Sydney", "NSW", "AUS")

initializer.req()


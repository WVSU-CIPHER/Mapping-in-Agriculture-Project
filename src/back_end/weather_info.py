# returns weather information of the current hour at latitude and longitude

import requests
from config.settings import WEATHER_APIS

class WeatherData:
    def __init__(self):
        self.base_url = WEATHER_APIS[1]["api_url"]
        self.weather_data = None

    def fetch_weather_data(self, latitude, longitude):
        params = WEATHER_APIS[1]["params"].copy()
        params.update({"latitude": latitude, "longitude": longitude}) 

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            self.weather_data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            self.weather_data = None

    def get_temperature(self):
        try:
            return self.weather_data['current_weather']['temperature']
        except KeyError:
            print("Temperature data is missing.")
            return None

    def get_humidity(self):
        try:
            return self.weather_data['hourly']['relative_humidity_2m'][0]
        except KeyError:
            print("Humidity data is missing.")
            return None

    def get_wind_speed(self):
        try:
            return self.weather_data['current_weather']['windspeed']
        except KeyError:
            print("Wind speed data is missing.")
            return None

    def get_rainfall(self):
        try:
            return self.weather_data['hourly']['rain'][0]
        except KeyError:
            print("Rainfall data is missing.")
            return None

    def _calculate_heat_index(self, temperature, humidity):
        temp_f = (temperature * 9 / 5) + 32

        constants = [-42.379, 2.04901523, 10.14333127, -0.22475541, -0.00683783, -0.05481717, 0.00122874, 0.00085282, -0.00000199]

        temp_f_sq = temp_f ** 2
        humidity_sq = humidity ** 2
        heat_index_f = (
            constants[0] +
            constants[1] * temp_f +
            constants[2] * humidity +
            constants[3] * temp_f * humidity +
            constants[4] * temp_f_sq +
            constants[5] * humidity_sq +
            constants[6] * temp_f_sq * humidity +
            constants[7] * temp_f * humidity_sq +
            constants[8] * temp_f_sq * humidity_sq
        )
        
        heat_index_c = (heat_index_f - 32) * 5/9
        return round(heat_index_c, 2)

    def get_heat_index(self):
        try:
            temperature = self.get_temperature()
            humidity = self.get_humidity()
            if temperature is not None and humidity is not None:
                return self._calculate_heat_index(temperature, humidity)
            else:
                return None
        except KeyError:
            print("Error calculating heat index.")
            return None

# # [testing purposes]
# if __name__ == "__main__":
#     LATITUDE = 10.3157
#     LONGITUDE = 123.8854

#     weather = WeatherData()
#     weather.fetch_weather_data(LATITUDE, LONGITUDE)

#     temperature = weather.get_temperature()
#     humidity = weather.get_humidity()
#     wind_speed = weather.get_wind_speed()
#     rainfall = weather.get_rainfall()
#     heat_index = weather.get_heat_index()

#     print(f"Weather at coordinates ({LATITUDE}, {LONGITUDE}):")
#     print(f"Temperature: {temperature} °C" if temperature is not None else "Temperature: Data unavailable")
#     print(f"Humidity: {humidity} %" if humidity is not None else "Humidity: Data unavailable")
#     print(f"Rainfall (current hour): {rainfall} mm" if rainfall is not None else "Rainfall: Data unavailable")
#     print(f"Wind Speed: {wind_speed} m/s" if wind_speed is not None else "Wind Speed: Data unavailable")
#     print(f"Heat Index: {heat_index} °C" if heat_index is not None else "Heat Index: Data unavailable")
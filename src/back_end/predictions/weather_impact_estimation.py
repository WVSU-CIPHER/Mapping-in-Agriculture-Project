# returns risk levels for each predicted future weather conditions to be used for success_rate_prediction and harvest_date_estimation

import requests
from typing import Dict, Optional
from back_end.config.settings import WEATHER_APIS

class CropWeatherImpact:
    def __init__(self):
        # initializes api and data sets
        self.base_url = WEATHER_APIS[0]["api_url"]
        self.weather_forecast = []
        self.elevation = None

    def fetch_weather_data(self, latitude: float, longitude: float):
        # gets weather data via api
        # arg. latitude: current latitude of the location
        # arg. longitude: current longitude of the location
        # return: response from api
        params = WEATHER_APIS[0]["params"].copy()
        params.update({"latitude": latitude, "longitude": longitude}) 

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            weather_data = response.json()
            self._parse_weather_data(weather_data)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            self.weather_forecast = []

    def _parse_weather_data(self, weather_data: Dict):
        # separates data for each parameter
        # arg. weather_data: response from api in json form
        daily_forecasts = weather_data.get('daily', {})
        dates = daily_forecasts.get('time', [])
        max_temps = daily_forecasts.get('temperature_2m_max', [])
        min_temps = daily_forecasts.get('temperature_2m_min', [])
        precipitations = daily_forecasts.get('precipitation_sum', [])
        max_wind_speeds = daily_forecasts.get('windspeed_10m_max', [])

        self.weather_forecast = [
            {
                "day": dates[i],
                "temperature_max": max_temps[i],
                "temperature_min": min_temps[i],
                "precipitation": precipitations[i],
                "wind_speed": max_wind_speeds[i]
            }
            for i in range(len(dates))
        ]

        self.elevation = weather_data.get("elevation", None)

    def get_weather_data_for_day(self, day_index: int) -> Optional[Dict[str, float]]:
        # returns weather data of a certain day
        # arg. day_index: day in index (0: current, 1: next day, ...so on)
        # return: weather forecast in dictionary
        if 0 <= day_index < len(self.weather_forecast):
            return self.weather_forecast[day_index]
        return None

    def get_temperature(self, day_index: int) -> Optional[float]:
        # returns temperature (Celsius) of a certain day
        # arg. day_index: day in index (0: current, 1: next day, ...so on)
        # return: temperature (Celsius)
        day = self.get_weather_data_for_day(day_index)
        return day.get("temperature_max") if day else None

    def get_precipitation(self, day_index: int) -> Optional[float]:
        # returns precipitation (mm) of a certain day
        # arg. day_index: day in index (0: current, 1: next day, ...so on)
        # return: precipitation (mm)
        day = self.get_weather_data_for_day(day_index)
        return day.get("precipitation") if day else None

    def get_wind_speed(self, day_index: int) -> Optional[float]:
        # returns wind speed (m/s) of a certain day
        # arg. day_index: day in index (0: current, 1: next day, ...so on)
        # return: wind speed (m/s)
        day = self.get_weather_data_for_day(day_index)
        return day.get("wind_speed") if day else None

    def get_temperature_risk_level(self, value: float) -> str:
        # returns risk level based on the value of temperature
        # arg. value: value of weather temperature
        # return: temperature risk level
        thresholds = {
            "High": (-float("inf"), 0),
            "Moderate": (0, 5),
            "Low": (5, 30),
            "Moderate": (30, 35),
            "High": (35, float("inf"))
        }
        return self._get_risk_level(value, thresholds)

    def get_precipitation_risk_level(self, value: float) -> str:
        # returns risk level based on the value of precipitation
        # arg. value: value of weather precipitation
        # return: precipitation risk level
        thresholds = {
            "High": (50, float("inf")),
            "Moderate": (20, 50),
            "Low": (0, 20)
        }
        return self._get_risk_level(value, thresholds)

    def get_wind_speed_risk_level(self, value: float) -> str:
        # returns risk level based on the value of wind speed
        # arg. value: value of weather wind speed
        # return: wind speed risk level
        thresholds = {
            "High": (20, float("inf")),
            "Moderate": (10, 20),
            "Low": (0, 10)
        }
        return self._get_risk_level(value, thresholds)

    def get_overall_risk(self, day_index: int) -> Optional[str]:
        # returns the overall risk calculated from temperature, precipitation, and wind speed risk levels
        # arg. day_index: day in index (0: current, 1: next day, ...so on)
        # return: overall risk level
        day = self.get_weather_data_for_day(day_index)
        if not day:
            return None

        temperature = self.get_temperature(day_index)
        precipitation = self.get_precipitation(day_index)
        wind_speed = self.get_wind_speed(day_index)

        temperature_risk = self.get_temperature_risk_level(temperature) if temperature is not None else "Low"
        precipitation_risk = self.get_precipitation_risk_level(precipitation) if precipitation is not None else "Low"
        wind_risk = self.get_wind_speed_risk_level(wind_speed) if wind_speed is not None else "Low"

        risk_values = {"Low": 0, "Moderate": 1, "High": 2}

        # calculate average risk level
        avg_risk = (risk_values[temperature_risk] + 
                    risk_values[precipitation_risk] + 
                    risk_values[wind_risk]) / 3.0

        if avg_risk < 0.67:
            return "Low"
        elif avg_risk < 1.33:
            return "Moderate"
        else:
            return "High"

    def _get_risk_level(self, value: float, thresholds: Dict[str, tuple]) -> str:
        return next((risk for risk, (low, high) in thresholds.items() if low <= value <= high), "Low")
    
    def get_elevation(self) -> Optional[float]:
        # returns the elevation based on latitude and longitude
        return self.elevation

# # [testing purposes]
# if __name__ == "__main__":
#     latitude = 10.3157
#     longitude = 123.8854

#     analyzer = CropWeatherImpact()
#     analyzer.fetch_weather_data(latitude, longitude)

#     day_index = 0
#     print(f"Temperature for day {day_index}: {analyzer.get_temperature(day_index)}")
#     print(f"Temperature risk level for day {day_index}: {analyzer.get_temperature_risk_level(day_index)}")
#     print(f"Precipitation for day {day_index}: {analyzer.get_precipitation(day_index)}")
#     print(f"Precipitation risk level for day {day_index}: {analyzer.get_precipitation_risk_level(day_index)}")
#     print(f"Wind speed for day {day_index}: {analyzer.get_wind_speed(day_index)}")
#     print(f"Wind speed risk level for day {day_index}: {analyzer.get_wind_speed_risk_level(day_index)}")
#     print(f"Overall risk for day {day_index}: {analyzer.get_overall_risk(day_index)}")
#     print(f"Elevation: {analyzer.get_elevation()}")
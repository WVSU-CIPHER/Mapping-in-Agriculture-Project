# returns success rates based on processed images

import pandas as pd
from config.settings import SUCCESS_RATE_WEIGHTED_AVERAGE as success_weight

class CropSuccessRate:
    def __init__(self):
        # loads dataset
        # arg. csv_path: path to the csv file containing crop datas
        self.data = self._load_data()

    def _load_data(self):
        # loads data from all CSV
        data = {}
        data["global_crop_data"] = pd.read_csv("./src/back_end/data/global_crop_data.csv")
        data["geolocation_ranges"] = pd.read_csv("./src/config/geolocation_ranges.csv")
        return data
    
    def _calculate_geolocation_score(self, latitude: float, elevation: float) -> float:
        # calculates the geolocation score based on the coordinate and elevation
        # arg. latitude: latitude of the location
        # arg. longitude: longitude of the location
        # arg. elevation: elevation of the location
        # return: geolocation impact score

        # calculates distance from equator
        distance_from_equator = abs(latitude)
        data = self.data["geolocation_ranges"]

        # matches the geolocation impact based on ranges
        for _, row in data.iterrows():
            if (
                row["distance_from_equator_min"] <= distance_from_equator <= row["distance_from_equator_max"]
                and row["elevation_min"] <= elevation <= row["elevation_max"]
            ):
                return row["score"]

        return 0.1  # defaults to low score for undefined ranges

    def _calculate_temperature_score(self, weather_temperature: float, min_thresold_temperature: float, max_thresold_temperature: float) -> float:
        # calculates the temperature score affecting thresholds
        # arg. weather_temperature: current temperature in celsius
        # arg. min_threshold_temperature: minimum temperature a crop can withstand
        # arg. max_threshold_temperature: maximum temperature a crop can withstand
        # return: temperature imapct score
        if weather_temperature < min_thresold_temperature or weather_temperature > max_thresold_temperature:
            return 0.0
        score = (weather_temperature - min_thresold_temperature) / (max_thresold_temperature - min_thresold_temperature) 
        return score
    
    def _calculate_precipitation_score(self, weather_precipitation: float, water_requirement: float, drought_tolerance: float) -> float:
        # calculates the precipitation score affecting of water requirement and drought tolerance
        # arg. weather_precipitation: current precipitation in mm
        # arg. water_requirement: water requirement for crop daily in mm
        # arg. drought_tolerance: drought tolerance level of the crop in percentage
        # return: precipitation impact score
        lower_bound = water_requirement * (1 - drought_tolerance / 100)
        upper_bound = water_requirement * (1 + drought_tolerance / 100)

        if weather_precipitation < lower_bound or weather_precipitation > upper_bound:
            return 0.0
        score = 1.0 - abs(weather_precipitation - water_requirement) / water_requirement
        return score
    
    def _calculate_wind_speed_score(self, weather_wind_speed: float, wind_tolerance: float) -> float:
        # calculates the wind speed score affecting of tolerance
        # arg. weather_wind_speed: current wind speed in km/h
        # arg. wind_tolerance: wind tolerance level of the crop in percentage
        # return: wind impact score
        max_tolerated_speed = (wind_tolerance / 100) * 100  # Convert percentage to km/h
        if weather_wind_speed > max_tolerated_speed:
            return 0.0
        score = 1.0 - weather_wind_speed / max_tolerated_speed
        return score
    
    def _get_global_crop_data(self, crop_name: str):
        # retrieves crop data from the predefined data sets in csv
        # arg. crop_name: name of the crop in string
        # arg. disease_name: name of the disease in string
        # return: data row based on crop and disease name
        global_crop_data = self.data["global_crop_data"]
        crop_row = global_crop_data[
            (global_crop_data["crop_name"].str.lower().replace(" ", "_") == crop_name.lower().replace(" ", "_"))
        ]
        if crop_row.empty:
            raise ValueError("Crop and disease combination not found.")
        return crop_row.iloc[0]
    
    def calculate_success_rate(self, crop_name: str, latitude: float, elevation: float, weather_temperature: float, weather_precipitation: float, weather_wind_speed: float, disease_risk_value: float) -> float:
        # calculates the success rate of a crop
        # arg. crop_name: name of the crop in string
        # arg. latitude: latitude of the location
        # arg. elevation: elevation of the location
        # arg. weather_temperature: current temperature of the weather
        # arg. weather_precipitation: current precipitation (mm) of the weather
        # arg. weather_wind_speed: current wind speed (km/h) of the weather
        # arg. disease_risk_value: risk value from disease risk prediction 
        # return: success rate in float (normalized [0,1])

        # gets crop-specific data
        crop_data = self._get_global_crop_data(crop_name)
        min_threshold_temperature = crop_data["min_threshold_temperature"]
        max_threshold_temperature = crop_data["max_threshold_temperature"]
        water_requirement = crop_data["water_requirement"]
        drought_tolerance = crop_data["drought_tolerance"]
        wind_tolerance = crop_data["wind_tolerance"]

        # calculates individual scores with corresponding formula
        geolocation_score = self._calculate_geolocation_score(latitude, elevation)
        temperature_score = self._calculate_temperature_score(weather_temperature, min_threshold_temperature, max_threshold_temperature)
        precipitation_score = self._calculate_precipitation_score(weather_precipitation, water_requirement, drought_tolerance)
        wind_speed_score = self._calculate_wind_speed_score(weather_wind_speed, wind_tolerance)

        # combines scores with weighted average
        overall_score = (
            success_weight["geolocation_score_weight"] * geolocation_score + 
            success_weight["temperature_score_weight"] * temperature_score + 
            success_weight["precipitation_score_weight"] * precipitation_score + 
            success_weight["wind_speed_score_weight"] * wind_speed_score +
            success_weight["disease_score_weight"] * disease_risk_value
        )
        return overall_score
    
# # [testing purposes]
# if __name__ == "__main__":
#     crop_disease_risk = CropSuccessRate()

#     # Sample input
#     crop_details = {
#         "crop_name": "Wheat",
#         "latitude": 10.25,
#         "elevation": 123.25,
#         "weather_temperature": 32.4,
#         "weather_precipitation": 400,
#         "weather_wind_speed": 5.3,
#         "disease_risk_value": 0.2
#     }

#     success_rate = crop_disease_risk.calculate_success_rate(**crop_details)
#     print(f"Success Rate: {success_rate}")
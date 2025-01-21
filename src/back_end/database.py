# manages interactions with the database for storing/retrieving data
# mainly to be used for field logs / history 

import os, json
from typing import List

class Database:
    def __init__(self):
        directory = "src/back_end/data"
        os.makedirs(directory, exist_ok=True)
        self.file_name = os.path.join(directory, "history_crop_data.json")

    def save_data(self, date: str, time: str, data: dict):
        # saves the provided data to the JSON file with the given date and time.
        # arg. date: current date in format YYYY-MM-DD
        # arg. time: current time in format HH-MM-SS
        # arg. data: crop data in json format
        entry = {
            "datetime": {
                "date": date,
                "time": time,
            },
            "data": data,
        }

        try:
            # loads existing data
            with open(self.file_name, "r") as file:
                database = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            # if file doesn't exist or is empty, initialize as empty list
            database = []

        # appends new entry
        database.append(entry)

        # saves back to file
        with open(self.file_name, "w") as file:
            json.dump(database, file, indent=4)

    def load_data(self, count: int) -> List[dict]:
        # loads the latest 'count' number of data entries from the JSON file.
        # arg. count: the number of data to be utilized
        # return: datas in json format
        try:
            # loads data from file
            with open(self.file_name, "r") as file:
                database = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

        # sorts data by date and time in descending order
        database.sort(
            key=lambda x: (x["datetime"]["date"], x["datetime"]["time"]),
            reverse=True,
        )

        # returns the latest 'count' entries
        actual_count = min(count, len(database))
        return database[:actual_count], actual_count

    def generate_json_string(self, date: str, time: str, data: dict) -> str:
        # generates a JSON-formatted string for the given date, time, and data.
        # arg. date: current date in format YYYY-MM-DD
        # arg. time: current time in format HH-MM-SS
        # arg. data: crop data in json format
        # return: json format of data in string
        entry = {
            "datetime": {
                "date": date,
                "time": time,
            },
            "data": data,
        }
        return json.dumps(entry, indent=4)

# # [testing purposes]
# if __name__ == "__main__":
#     db = Database()
#     # Example data
#     date = "2025-01-21"
#     time = "14:30:00"
#     crop_data = {
#         "crop_name": "Wheat",
#         "image_url": "https://crop.kindwise.com/media/images/db8c8e328f44427aaab12216e0cc3d5b.jpg",
#         "coordinate": {
#             "latitude": 12.3456,
#             "longitude": 78.9012,
#             "elevation": 123.45,
#         },
#         "disease_risks": {
#             "disease_name": "Rust",
#             "symptoms": "Yellow spots on leaves",
#             "severity": "Moderate",
#             "spreading": "Airborne",
#         },
#         "treatments": {
#             "preventions": "Crop rotation",
#             "chemical_treatment": "Fungicide X",
#             "biological_treatment": "Bacillus subtilis",
#         },
#         "prediction": {
#             "success_rate": 85.5,
#             "weather_impact": {
#                 "temperature": 25.5,
#                 "temperature_risk_level": "Low",
#                 "precipitation": 50.0,
#                 "precipitation_risk_level": "Moderate",
#                 "wind_speed": 10.0,
#                 "wind_speed_risk_level": "Low",
#                 "overall_risk_level": "Low",
#             },
#             "disease_impact": {
#                 "value": 20.0,
#                 "risk_level": "Moderate",
#             },
#             "suggestions": "Increase monitoring and use fungicide if necessary."
#         }
#     }

#     # Generate JSON string
#     json_string = db.generate_json_string(date, time, crop_data)
#     print("Generated JSON String:")
#     print(json_string)

#     # Save the data
#     db.save_data(date, time, crop_data)

#     # Load the latest 3 data entries
#     latest_data = db.load_data(3)
#     for entry in latest_data:
#         print("Date:", entry["datetime"]["date"])
#         print("Time:", entry["datetime"]["time"])
#         print("Crop Name:", entry["data"]["crop_name"])
#         print()
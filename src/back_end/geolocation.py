# returns the current latitude and longitude of a device dynamically
# (latitude, longitude)

import requests
from typing import Tuple

class GeoLocation:
    def __init__(self, ip_api_url: str = "https://ipinfo.io"):
        # initializes the GeoLocation class with the IP-based geolocation API URL.
        # arg. ip_api_url : URL of the IP-based geolocation API.
        self.ip_api_url = ip_api_url

    def get_current_location(self) -> Tuple[float, float]:
        # fetches the current latitude and longitude of the device's location.
        # return: tuple containing the latitude and longitude.
        try:
            # fetches data from the IP-based geolocation API
            response = requests.get(self.ip_api_url)
            response.raise_for_status()
            data = response.json()

            # parse latitude and longitude from the response
            location = data.get("loc", "")
            if not location:
                raise ValueError("Location data not available in the response.")

            latitude, longitude = map(float, location.split(","))
            return latitude, longitude

        except requests.RequestException as e:
            raise Exception(f"Failed to fetch location data: {e}")
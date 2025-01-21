# returns the current latitude and longitude of a device dynamically
# (latitude, longitude)

import requests
from typing import Tuple
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from datetime import datetime

class GeoLocation:
    def __init__(self, ip_api_url: str = "https://ipinfo.io"):
        # initializes the GeoLocation class with the IP-based geolocation API URL.
        # arg. ip_api_url : URL of the IP-based geolocation API.
        self.ip_api_url = ip_api_url
        self.geolocator = Nominatim(user_agent="my_app")

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
            return 10.712403, 122.560260    # default, to be removed
            raise Exception(f"Failed to fetch location data: {e}")
    
    def get_address_from_coordinates(self, latitude: float, longitude: float) -> str:
        try:
            location = self.geolocator.reverse((latitude, longitude))
            if location:
                address = location.raw.get('address', {})
                city = address.get('city', '')
                state = address.get('state', '')
                country = address.get('country', '')
                
                # Filter out empty components and join with commas
                components = [comp for comp in [city, state, country] if comp]
                if components:
                    return ", ".join(components)
                
            return "Unknown"
        except GeocoderTimedOut:
            return "Unknown"
        except Exception as e:
            return f"Unknown"
        
class DateTime:
    def get_current_weekday(self) -> str:
        # returns current day of the week
        weekday = datetime.now().strftime("%A")
        return str(weekday)
    
    def get_current_day(self) -> str:
        # returns formatted date string
        date = datetime.now().strftime("%d %b %Y")
        return str(date)
import requests
from src.api.base_api import BaseAPI

class AeroplanesAPI(BaseAPI):

    def get_coordinates(self, country: str):
        try:
            url = "https://nominatim.openstreetmap.org/search"
            params = {
                "q": country,
                "format": "json"
            }

            response = requests.get(url, params=params, timeout=10)
            data = response.json()

            bbox = data[0]["boundingbox"]

            return {
                "south": float(bbox[0]),
                "north": float(bbox[1]),
                "west": float(bbox[2]),
                "east": float(bbox[3]),
            }

        except Exception:
            return None

    def get_aeroplanes(self, country: str):
        coords = self.get_coordinates(country)

        if not coords:
            return []

        try:
            url = "https://opensky-network.org/api/states/all"

            params = {
                "lamin": coords["south"],
                "lomin": coords["west"],
                "lamax": coords["north"],
                "lomax": coords["east"],
            }

            response = requests.get(url, params=params, timeout=10)
            data = response.json()

            return data.get("states", [])

        except Exception:
            return []

from requests import get

from src.api.base_api import BaseAPI


class AeroplanesAPI(BaseAPI):

    def __init__(self):
        self.openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
        self.opensky_url = 'https://opensky-network.org/api/states/all'
        self.aeroplanes = None

    def get_coordinates(self, country: str):
        try:
            headers = {'User-Agent': 'test-app/1.0'}
            params = {'country': country, 'format': 'json', 'limit': 1}

            response = get(url=self.openstreetmap_url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()

            if not data:
                print("No data returned from OSM")
                return None

            bbox = data[0]['boundingbox']
            coords = {
                'south': float(bbox[0]),
                'north': float(bbox[1]),
                'west': float(bbox[2]),
                'east': float(bbox[3]),
            }
            print("Coordinates found:", coords)
            return coords

        except Exception as e:
            print("Error in get_coordinates:", e)
            return None

    def get_aeroplanes(self, country: str):
        coords = self.get_coordinates(country)
        if not coords:
            print("No coordinates, returning empty list")
            return []

        try:
            params = {
                'lamin': coords['south'],
                'lamax': coords['north'],
                'lomin': coords['west'],
                'lomax': coords['east'],
            }
            response = get(self.opensky_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            print("Number of aeroplanes received:", len(data.get('states', [])))
            return data.get('states', [])
        except Exception as e:
            print("Error fetching aeroplanes:", e)
            return []

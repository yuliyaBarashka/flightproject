import json
from src.storage.base_storage import BaseStorage

class JSONSaver(BaseStorage):

    def __init__(self, filename="data.json"):
        self.filename = filename

    def add(self, plane):
        data = self.get_all()

        data.append(plane.__dict__)

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def get_all(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except:
            return []

    def delete(self, plane):
        data = self.get_all()

        data = [p for p in data if p["callsign"] != plane.callsign]

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)
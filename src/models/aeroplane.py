class Aeroplane:

    def __init__(self, callsign: str, country: str, velocity: float, altitude: float):
        self.callsign = callsign.strip() if callsign else "Unknown"
        self.country = country or "Unknown"
        self.velocity = float(velocity) if velocity else 0.0
        self.altitude = float(altitude) if altitude else 0.0

    def __repr__(self):
        return f"{self.callsign} | {self.country} | {self.velocity} m/s | {self.altitude} m"

    # сравнение по скорости
    def __lt__(self, other):
        return self.velocity < other.velocity

    # сравнение по высоте
    def __gt__(self, other):
        return self.altitude > other.altitude

    @classmethod
    def cast_to_object_list(cls, data):
        result = []

        for item in data:
            try:
                plane = cls(
                    callsign=item[1],
                    country=item[2],
                    velocity=item[9],
                    altitude=item[13],
                )
                result.append(plane)
            except Exception:
                continue

        return result

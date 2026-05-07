def filter_by_country(planes, countries):
    return [p for p in planes if p.country in countries]

def sort_by_altitude(planes):
    return sorted(planes, key=lambda x: x.altitude, reverse=True)

def get_top_n(planes, n):
    return planes[:n]

def filter_by_altitude_range(planes, range_str):
    try:
        min_h, max_h = map(float, range_str.split("-"))
        return [p for p in planes if min_h <= p.altitude <= max_h]
    except:
        return planes

from src.models.aeroplane import Aeroplane
from src.utils import filter_by_altitude_range, filter_by_country, get_top_n, sort_by_altitude


def sample_planes():
    return [
        Aeroplane("A", "USA", 200, 1000),
        Aeroplane("B", "UK", 250, 1500),
        Aeroplane("C", "USA", 300, 1200),
        Aeroplane("D", "FR", 180, 800),
    ]


def test_filter_by_country():
    planes = sample_planes()
    filtered = filter_by_country(planes, ["USA", "FR"])
    assert len(filtered) == 3
    assert all(p.country in ["USA", "FR"] for p in filtered)


def test_sort_by_altitude():
    planes = sample_planes()
    sorted_planes = sort_by_altitude(planes)
    altitudes = [p.altitude for p in sorted_planes]
    assert altitudes == sorted(altitudes, reverse=True)


def test_get_top_n():
    planes = sample_planes()
    top2 = get_top_n(planes, 2)
    assert len(top2) == 2
    assert top2 == planes[:2]


def test_filter_by_altitude_range():
    planes = sample_planes()
    filtered = filter_by_altitude_range(planes, "1000-1300")
    altitudes = [p.altitude for p in filtered]
    assert all(1000 <= alt <= 1300 for alt in altitudes)
    # Проверка некорректного ввода
    assert filter_by_altitude_range(planes, "invalid") == planes

from src.models.aeroplane import Aeroplane


def test_compare_speed():
    p1 = Aeroplane("A", "USA", 200, 1000)
    p2 = Aeroplane("B", "USA", 300, 2000)

    assert p1 < p2


def test_compare_altitude():
    p1 = Aeroplane("A", "USA", 200, 1000)
    p2 = Aeroplane("B", "USA", 300, 2000)

    assert p2 > p1


def test_cast():
    data = [[None, "ABC", "USA", None, None, None, None, None, None, 250, None, None, None, 10000]]
    planes = Aeroplane.cast_to_object_list(data)

    assert len(planes) == 1


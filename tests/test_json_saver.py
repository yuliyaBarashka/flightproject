import os
import json
import tempfile
from src.models.aeroplane import Aeroplane
from src.storage.json_saver import JSONSaver


def test_json_saver_add_and_file(tmp_path):
    file_path = tmp_path / "planes.json"
    saver = JSONSaver(file_path=str(file_path))

    plane = Aeroplane("A", "USA", 200, 1000)
    saver.add(plane)

    # Проверяем, что файл создался
    assert os.path.exists(file_path)

    # Проверяем содержимое
    with open(file_path, "r") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert data[0]["name"] == "A"
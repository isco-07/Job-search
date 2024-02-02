import json
import os

import pytest

from src.json_saver import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def temp_json_file():
    temp_file_path = os.path.join(os.path.dirname(__file__), "..", "tests/test_json_saver.json")
    return temp_file_path


def test_add_vacancy(temp_json_file: str) -> None:
    json_saver = JSONSaver()
    with open(temp_json_file, "w") as file:
        json.dump([], file)
    vacancy = Vacancy(name="Test Job", url="https://example.com/job1", salary="50000", experience="Junior")

    json_saver.add_vacancy(vacancy, temp_json_file)

    with open(temp_json_file, encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 1
    assert data[0]["name"] == "Test Job"
    assert data[0]["salary"] == "50000руб."
    assert data[0]["experience"] == "Junior"


def test_get_vacancies_by_salary(temp_json_file: str) -> None:
    json_saver = JSONSaver()
    with open(temp_json_file, "w") as file:
        json.dump([], file)
    vacancy1 = Vacancy(name="Job1", url="https://example.com/job1", salary="60000", experience="Mid-level")
    vacancy2 = Vacancy(name="Job2", url="https://example.com/job2", salary="60000", experience="Senior")

    json_saver.add_vacancy(vacancy1, temp_json_file)
    json_saver.add_vacancy(vacancy2, temp_json_file)

    result = json_saver.get_vacancies_by_salary("60000руб.", temp_json_file)

    assert len(result) == 2
    assert result[0]["name"] == "Job1"
    assert result[1]["name"] == "Job2"


def test_delete_vacancy(temp_json_file: str) -> None:
    json_saver = JSONSaver()
    with open(temp_json_file, "w") as file:
        json.dump([], file)
    vacancy = Vacancy(name="JobToDelete", url="https://example.com/job1", salary="70000", experience="Senior")

    json_saver.add_vacancy(vacancy, temp_json_file)
    json_saver.delete_vacancy(vacancy, temp_json_file)

    with open(temp_json_file, encoding="utf-8") as file:
        data = json.load(file)

    assert len(data) == 0

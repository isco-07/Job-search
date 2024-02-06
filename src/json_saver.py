import json
import os

from src.json_job_handler import JSONJobHandler
from src.vacancy import Vacancy


class JSONSaver(JSONJobHandler):
    def add_vacancy(self, vacancy: Vacancy, path: str = "data/json_saver.json") -> None:
        """Добавляет в json файл словарь объекта Vacancy"""
        file_path = os.path.join(os.path.dirname(__file__), "..", path)
        try:
            with open(file_path, encoding="utf-8") as file:
                data = list(json.load(file))
        except FileNotFoundError:
            data = []
        data.append(
            {"name": vacancy.name, "url": vacancy.url, "salary": vacancy.salary, "experience": vacancy.experience}
        )
        with open(file_path, "w", encoding="utf-8") as file:

            json.dump(data, file, ensure_ascii=False, indent=2)

    def get_vacancies_by_salary(self, salary: str, path: str = "data/json_saver.json") -> list:
        """Возвращает список вакансий с указанной зарплатой"""
        file_path = os.path.join(os.path.dirname(__file__), "..", path)
        with open(file_path, encoding="utf-8") as file:
            json_load = json.load(file)

        return [i for i in json_load if i["salary"] == salary]

    def delete_vacancy(self, vacancy: Vacancy, path: str = "data/json_saver.json") -> None:
        """Удаляет вакансию из json файла, переданную в функцию"""
        file_path = os.path.join(os.path.dirname(__file__), "..", path)
        try:
            with open(file_path, encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        for i in data:
            if [vacancy.name, vacancy.url, vacancy.salary, vacancy.experience] == [
                i["name"],
                i["url"],
                i["salary"],
                i["experience"],
            ]:
                data.remove(i)
                break
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

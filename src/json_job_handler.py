from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class JSONJobHandler(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    def get_vacancies_by_salary(self, salary: str) -> None:
        pass

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        pass

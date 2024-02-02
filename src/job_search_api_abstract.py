from abc import ABC, abstractmethod


class JobSearchAPI(ABC):
    @abstractmethod
    def get_vacancies(self, key_word) -> None:
        pass

import requests

from src.job_search_api_abstract import JobSearchAPI


class HeadHunterAPI(JobSearchAPI):

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, key_word: str) -> list:
        """Получаем список вакансий с помощью api.hh.ru"""
        params = {"per_page": "100", "text": key_word}
        vacancies = []
        try:
            data = requests.get(url=self.__url, params=params).json()
            for vacancy in data["items"]:
                if vacancy["salary"] is not None:
                    if vacancy["salary"]["currency"] == "RUR":
                        salary = (
                            int(vacancy["salary"]["to"])
                            if vacancy["salary"]["to"] is not None
                            else int(vacancy["salary"]["from"])
                        )

                        vacancies.append(
                            {
                                "name": vacancy["name"],
                                "url": vacancy["url"],
                                "salary": f"{salary}руб.",
                                "experience": vacancy["experience"]["name"],
                            }
                        )
            return vacancies
        except requests.exceptions.ConnectionError as err:
            raise requests.exceptions.ConnectionError("HTTP Error:", err)

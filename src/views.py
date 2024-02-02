import json

from src.headhunterapi import HeadHunterAPI


def filter_vacancies(hh_vacancies: list, words: list) -> list:
    """Фильтрует список вакансий по ключевым словам"""
    vacancies = []
    words = [word.lower() for word in words]
    for vacancy in hh_vacancies:
        for word in words:
            if word in vacancy["name"].lower():
                vacancies.append(vacancy)
                break
    return vacancies


def sort_vacancies(vacancies: list) -> list:
    """Сортирует список вакансий по зарплате по убыванию"""
    return sorted(vacancies, key=lambda x: x["salary"], reverse=True)


def get_top_vacancies(vacancies: list, num: int) -> list:
    """Возвращает список вакансий равный num в случае если num <= длинны списка вакансий,
    либо список целиком"""
    return vacancies[:num] if len(vacancies) >= num else vacancies


def print_vacancies(vacancies: list) -> None:
    """Выводит в консоль список переданных в функцию вакансий"""
    for vacancy in vacancies:
        print(json.dumps(vacancy, ensure_ascii=False, indent=2))


def user_interaction() -> None:
    """Функция для взаимодействия с пользователем"""
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hh_api.get_vacancies(search_query)
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    filtered_vacancies = filter_vacancies(hh_vacancies, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = sort_vacancies(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)

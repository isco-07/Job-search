from src import views
from src.json_saver import JSONSaver
from src.vacancy import Vacancy

if __name__ == "__main__":
    # Создание экземпляра класса для работы с вакансиями
    vacancy = Vacancy(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        "100 000-150 000 руб.",
        "Требования: опыт работы от 3 лет...",
    )

    # Сохранение информации о вакансиях в файл
    json_saver = JSONSaver()
    json_saver.add_vacancy(vacancy)
    json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
    json_saver.delete_vacancy(vacancy)

    # Вызов функции для взаимодействия с пользователем
    views.user_interaction()

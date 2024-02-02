class Vacancy:
    # Инициализация объекта класса
    def __init__(self, name: str, url: str, salary: str, experience: str) -> None:
        self.name = name
        self.url = url
        self.salary = f"{max([int(" ".join(filter(lambda x: x.isdigit(), i))) for i in salary.split(" - ")])}руб."
        self.experience = experience

    # Строковое представление объекта класса
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.url}, {self.salary}, {self.experience})"

    # методы сравнения экземпляров класс Vacancy
    def __eq__(self, other) -> bool:
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        else:
            raise TypeError("Объекты разного типа данных")

    def __ne__(self, other) -> bool:
        if isinstance(other, Vacancy):
            return self.salary != other.salary
        else:
            raise TypeError("Объекты разного типа данных")

    def __lt__(self, other) -> bool:
        if isinstance(other, Vacancy):

            return self.salary < other.salary
        else:
            raise TypeError("Объекты разного типа данных")

    def __le__(self, other) -> bool:
        if isinstance(other, Vacancy):
            return self.salary <= other.salary
        else:
            raise TypeError("Объекты разного типа данных")

    def __gt__(self, other) -> bool:
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        else:
            raise TypeError("Объекты разного типа данных")

    def __ge__(self, other) -> bool:
        if isinstance(other, Vacancy):
            return self.salary >= other.salary
        else:
            raise TypeError("Объекты разного типа данных")

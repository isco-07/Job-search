class Vacancy:
    __slots__ = ("name", "url", "salary", "experience")

    def __init__(self, name: str, url: str, salary: str, experience: str) -> None:
        """Инициализация объекта класса"""
        self.name = name
        self.url = url
        self.salary = f"{max([int("".join(filter(lambda x: x.isdigit(), i))) for i in salary.split(" - ")])}руб."
        self.experience = experience

    def __repr__(self) -> str:
        """Строковое представление объекта класса"""
        return f"{self.__class__.__name__}({self.name}, {self.url}, {self.salary}, {self.experience})"

    def __eq__(self, other) -> bool:
        """метод сравнения на равенство экземпляров класс Vacancy"""
        if isinstance(other, Vacancy):
            return self.salary == other.salary
        else:
            raise TypeError("Объекты разного типа данных")

    def __ne__(self, other) -> bool:
        """метод неравенства экземпляров класс Vacancy"""
        if isinstance(other, Vacancy):
            return self.salary != other.salary
        else:
            raise TypeError("Объекты разного типа данных")

    def __lt__(self, other) -> bool:
        """метод сравнения на меньше экземпляров класс Vacancy"""
        if isinstance(other, Vacancy):

            return self.salary < other.salary
        else:
            raise TypeError("Объекты разного типа данных")

    def __le__(self, other) -> bool:
        """метод сравнения на меньше либо равно экземпляров класс Vacancy"""
        if isinstance(other, Vacancy):
            return self.salary <= other.salary
        else:
            raise TypeError("Объекты разного типа данных")

    def __gt__(self, other) -> bool:
        """метод сравнения на больше экземпляров класс Vacancy"""
        if isinstance(other, Vacancy):
            return self.salary > other.salary
        else:
            raise TypeError("Объекты разного типа данных")

    def __ge__(self, other) -> bool:
        """метод сравнения на больше либо равно экземпляров класс Vacancy"""
        if isinstance(other, Vacancy):
            return self.salary >= other.salary
        else:
            raise TypeError("Объекты разного типа данных")

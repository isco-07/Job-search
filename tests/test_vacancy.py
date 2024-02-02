import unittest

from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):

    def test_equality(self):
        vacancy1 = Vacancy(name="Job1", url="https://example.com/job1", salary="50000-70000", experience="Mid-level")
        vacancy2 = Vacancy(name="Job2", url="https://example.com/job2", salary="50000-70000", experience="Mid-level")

        self.assertEqual(vacancy1, vacancy2)

    def test_inequality(self):
        vacancy1 = Vacancy(name="Job1", url="https://example.com/job1", salary="50000-70000", experience="Mid-level")
        vacancy2 = Vacancy(name="Job2", url="https://example.com/job2", salary="60000-80000", experience="Senior")

        self.assertNotEqual(vacancy1, vacancy2)

    def test_less_than(self):
        vacancy1 = Vacancy(name="Job1", url="https://example.com/job1", salary="50000-70000", experience="Mid-level")
        vacancy2 = Vacancy(name="Job2", url="https://example.com/job2", salary="60000-80000", experience="Senior")

        self.assertLess(vacancy1, vacancy2)

    def test_greater_than(self):
        vacancy1 = Vacancy(name="Job1", url="https://example.com/job1", salary="60000-80000", experience="Senior")
        vacancy2 = Vacancy(name="Job2", url="https://example.com/job2", salary="50000-70000", experience="Mid-level")

        self.assertGreater(vacancy1, vacancy2)

    def test_less_than_or_equal(self):
        vacancy1 = Vacancy(name="Job1", url="https://example.com/job1", salary="50000-70000", experience="Mid-level")
        vacancy2 = Vacancy(name="Job2", url="https://example.com/job2", salary="50000-70000", experience="Mid-level")

        self.assertLessEqual(vacancy1, vacancy2)

    def test_greater_than_or_equal(self):
        vacancy1 = Vacancy(name="Job1", url="https://example.com/job1", salary="60000-80000", experience="Senior")
        vacancy2 = Vacancy(name="Job2", url="https://example.com/job2", salary="50000-70000", experience="Mid-level")

        self.assertGreaterEqual(vacancy1, vacancy2)

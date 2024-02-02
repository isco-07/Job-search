import json
from unittest.mock import MagicMock, call, patch

import pytest

from src.headhunterapi import HeadHunterAPI
from src.views import filter_vacancies, get_top_vacancies, print_vacancies, sort_vacancies, user_interaction


@pytest.fixture
def mock_hh_api():
    return MagicMock(spec=HeadHunterAPI)


def test_filter_vacancies() -> None:
    hh_vacancies = [
        {"name": "Software Developer", "salary": 80000},
        {"name": "Data Scientist", "salary": 90000},
        {"name": "Marketing Manager", "salary": 75000},
    ]
    filtered_vacancies = filter_vacancies(hh_vacancies, ["software", "developer"])
    assert len(filtered_vacancies) == 1
    assert filtered_vacancies[0]["name"] == "Software Developer"


def test_sort_vacancies() -> None:
    vacancies = [
        {"name": "Software Developer", "salary": 80000},
        {"name": "Data Scientist", "salary": 90000},
        {"name": "Marketing Manager", "salary": 75000},
    ]
    sorted_vacancies = sort_vacancies(vacancies)
    assert sorted_vacancies[0]["name"] == "Data Scientist"
    assert sorted_vacancies[-1]["name"] == "Marketing Manager"


def test_get_top_vacancies() -> None:
    vacancies = [
        {"name": "Software Developer", "salary": 80000},
        {"name": "Data Scientist", "salary": 90000},
        {"name": "Marketing Manager", "salary": 75000},
    ]
    top_vacancies = get_top_vacancies(vacancies, 2)
    assert len(top_vacancies) == 2


@patch("builtins.print")
def test_print_vacancies(mock_print) -> None:
    vacancies = [
        {"name": "Software Developer", "salary": 80000},
        {"name": "Data Scientist", "salary": 90000},
    ]
    expected_calls = [
        ((json.dumps(vacancies[0], ensure_ascii=False, indent=2),), {}),
        ((json.dumps(vacancies[1], ensure_ascii=False, indent=2),), {}),
    ]

    print_vacancies(vacancies)
    mock_print.assert_has_calls(expected_calls, any_order=True)


@patch("builtins.input", side_effect=["Software Developer", "3", "software developer"])
@patch("src.headhunterapi.HeadHunterAPI")
def test_user_interaction(mock_api, mock_input) -> None:
    user_interaction()

    expected_calls = [
        call("Введите поисковый запрос: "),
        call("Введите количество вакансий для вывода в топ N: "),
        call("Введите ключевые слова для фильтрации вакансий: "),
    ]

    assert mock_input.call_args_list == expected_calls
    # mock_api.return_value.get_vacancies.assert_called_with("Software Developer")

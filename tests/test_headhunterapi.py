import unittest
from unittest.mock import MagicMock, patch

import pytest
import requests

from src.headhunterapi import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):

    @patch("requests.get")
    def test_get_vacancies_success(self, mock_get) -> None:
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "items": [
                {
                    "name": "Job 1",
                    "url": "https://example.com/job1",
                    "salary": {"from": 50000, "to": 80000, "currency": "RUR"},
                    "experience": {"name": "Mid-level"},
                },
            ]
        }
        mock_get.return_value = mock_response

        hh_api = HeadHunterAPI()
        result = hh_api.get_vacancies("python")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["name"], "Job 1")
        self.assertEqual(result[0]["url"], "https://example.com/job1")
        self.assertEqual(result[0]["salary"], "80000руб.")
        self.assertEqual(result[0]["experience"], "Mid-level")

    @patch("requests.get")
    def test_get_vacancies_connection_error(self, mock_get) -> None:
        mock_get.side_effect = requests.exceptions.ConnectionError("Fake Connection Error")

        hh_api = HeadHunterAPI()

        with pytest.raises(requests.exceptions.ConnectionError):
            hh_api.get_vacancies("python")

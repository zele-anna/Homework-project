from unittest.mock import patch

import pandas as pd

from src.reader import read_csv, read_excel

sample_df = pd.DataFrame(
    {
        "id": [650703, 3598919, 593027, 366176, 5380041],
        "state": ["EXECUTED", "EXECUTED", "CANCELED", "EXECUTED", "CANCELED"],
        "date": [
            "2023-09-05T11:30:32Z",
            "2020-12-06T23:00:58Z;29740",
            "2023-07-22T05:02:01Z",
            "2020-08-02T09:35:18Z",
            "2021-02-01T11:54:58Z",
        ],
        "amount": [16210, 29740, 30368, 29482, 23789],
        "currency_name": ["Sol", "Peso", "Shilling", "Rupiah", "Peso"],
        "currency_code": ["PEN", "COP", "TZS", "IDR", "UYU"],
        "from": [
            "Счет 58803664561298323391",
            "Discover 3172601889670065",
            "Visa 1959232722494097",
            "Discover 0325955596714937",
            "",
        ],
        "to": [
            "Счет 39745660563456619397",
            "Discover 0720428384694643",
            "Visa 6804119550473710",
            "Visa 3820488829287420",
            "Счет 23294994494356835683",
        ],
        "description": [
            "Перевод организации",
            "Перевод с карты на карту",
            "Перевод с карты на карту",
            "Перевод с карты на карту",
            "Открытие вклада",
        ],
    }
)

expected_result = [
    {
        "amount": 16210,
        "currency_code": "PEN",
        "currency_name": "Sol",
        "date": "2023-09-05T11:30:32Z",
        "description": "Перевод организации",
        "from": "Счет 58803664561298323391",
        "id": 650703,
        "state": "EXECUTED",
        "to": "Счет 39745660563456619397",
    },
    {
        "amount": 29740,
        "currency_code": "COP",
        "currency_name": "Peso",
        "date": "2020-12-06T23:00:58Z;29740",
        "description": "Перевод с карты на карту",
        "from": "Discover 3172601889670065",
        "id": 3598919,
        "state": "EXECUTED",
        "to": "Discover 0720428384694643",
    },
    {
        "amount": 30368,
        "currency_code": "TZS",
        "currency_name": "Shilling",
        "date": "2023-07-22T05:02:01Z",
        "description": "Перевод с карты на карту",
        "from": "Visa 1959232722494097",
        "id": 593027,
        "state": "CANCELED",
        "to": "Visa 6804119550473710",
    },
    {
        "amount": 29482,
        "currency_code": "IDR",
        "currency_name": "Rupiah",
        "date": "2020-08-02T09:35:18Z",
        "description": "Перевод с карты на карту",
        "from": "Discover 0325955596714937",
        "id": 366176,
        "state": "EXECUTED",
        "to": "Visa 3820488829287420",
    },
    {
        "amount": 23789,
        "currency_code": "UYU",
        "currency_name": "Peso",
        "date": "2021-02-01T11:54:58Z",
        "description": "Открытие вклада",
        "from": "",
        "id": 5380041,
        "state": "CANCELED",
        "to": "Счет 23294994494356835683",
    },
]


@patch("src.reader.pd.read_csv")
def test_read_csv(mock_reader) -> None:
    """Тест на чтение файла csv."""
    mock_reader.return_value = sample_df
    assert read_csv("test.scv") == expected_result


def test_read_csv_no_file() -> None:
    """Тест, если файл csv не найден."""
    assert read_excel("test.csv") == []


@patch("src.reader.pd.read_excel")
def test_read_excel(mock_reader) -> None:
    """Тест на чтение файла xlsx."""
    mock_reader.return_value = sample_df
    assert read_excel("test.xlsx") == expected_result


def test_read_excel_no_file() -> None:
    """Тест, если файл excel не найден."""
    assert read_excel("test.xlsx") == []

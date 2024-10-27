from collections import Counter

from src.search import category_counter, search_via_description


def test_search_via_description_json_data(json_data: list[dict]) -> None:
    assert search_via_description(list(json_data), "перевод") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": 31957.58, "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 441945886,
            "state": "CANCELED",
            "date": "2019-10-26T10:50:58.294041",
            "operationAmount": {"amount": 200.00, "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод с карты на карту",
            "from": "Maestro 1596837868705200",
            "to": "Счет 64686473678894779200",
        },
    ]
    assert search_via_description(list(json_data), "123") == []
    assert search_via_description(list(json_data), "вклад") == [
        {
            "id": 441945887,
            "state": "PENDING",
            "date": "2019-09-26T10:50:58.294041",
            "operationAmount": {"amount": 100.00, "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
            "to": "Счет 64686473678894779100",
        }
    ]


def test_search_via_description_csv_or_excel_data(csv_or_excel_data: list[dict]) -> None:
    assert search_via_description(list(csv_or_excel_data), "перевод") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "amount": 31957.58,
            "currency_name": "руб.",
            "currency_code": "RUB",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 441945886,
            "state": "CANCELED",
            "date": "2019-10-26T10:50:58.294041",
            "amount": 200.00,
            "currency_name": "EUR",
            "currency_code": "EUR",
            "description": "Перевод с карты на карту",
            "from": "Maestro 1596837868705200",
            "to": "Счет 64686473678894779200",
        },
    ]
    assert search_via_description(list(csv_or_excel_data), "123") == []
    assert search_via_description(list(csv_or_excel_data), "вклад") == [
        {
            "id": 441945887,
            "state": "PENDING",
            "date": "2019-09-26T10:50:58.294041",
            "amount": 100.00,
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Открытие вклада",
            "to": "Счет 64686473678894779100",
        }
    ]


def test_category_counter_json_data(json_data: list[dict]) -> None:
    category_list = ["Перевод организации", "Открытие вклада"]
    assert category_counter(json_data, category_list) == Counter({"Перевод организации": 1, "Открытие вклада": 1})


def test_category_counter_csv_or_excel_data(csv_or_excel_data: list[dict]) -> None:
    category_list = ["Перевод организации", "Открытие вклада"]
    assert category_counter(csv_or_excel_data, category_list) == Counter(
        {"Перевод организации": 1, "Открытие вклада": 1}
    )

import pytest


@pytest.fixture
def rub_transaction_data() -> dict:
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": 31957.58, "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def usd_transaction_data() -> dict:
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": 200.99, "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def eur_transaction_data() -> dict:
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": 100, "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def json_data() -> list[dict]:
    return [
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
            "id": 441945887,
            "state": "PENDING",
            "date": "2019-09-26T10:50:58.294041",
            "operationAmount": {"amount": 100.00, "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
            "to": "Счет 64686473678894779100",
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


@pytest.fixture
def csv_or_excel_data() -> list[dict]:
    return [
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
            "id": 441945887,
            "state": "PENDING",
            "date": "2019-09-26T10:50:58.294041",
            "amount": 100.00,
            "currency_name": "USD",
            "currency_code": "USD",
            "description": "Открытие вклада",
            "to": "Счет 64686473678894779100",
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

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions() -> list:
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 939719571,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 939719572,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод с карты на карту",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
        ),
        (
            "EUR",
            [
                {
                    "id": 939719572,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "EUR", "code": "EUR"}},
                    "description": "Перевод с карты на карту",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
        ),
    ],
)
def test_filter_by_currency(transactions: list, currency: str, expected: list) -> None:
    a = filter_by_currency(transactions, currency)
    assert list(a) == expected


def test_filter_by_currency_not_found(transactions: list) -> None:
    with pytest.raises(ValueError) as exc_info:
        filter_by_currency(transactions, "XXX")
    assert str(exc_info.value) == "Валюта не найдена"


def test_filter_by_currency_empty() -> None:
    with pytest.raises(ValueError) as exc_info:
        filter_by_currency([], "USD")
    assert str(exc_info.value) == "Список транзакций не задан"


def test_transaction_descriptions(transactions: dict) -> None:
    a = transaction_descriptions(transactions)
    assert next(a) == "Перевод организации"
    assert next(a) == "Перевод со счета на счет"
    assert next(a) == "Перевод с карты на карту"
    assert next(a) == "Перевод со счета на счет"


def test_transaction_descriptions_empty() -> None:
    with pytest.raises(ValueError) as exc_info:
        list(transaction_descriptions([]))
    assert str(exc_info.value) == "Список транзакций не задан"


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]),
        (999999999999, 1000000000001, ["0000 9999 9999 9999", "0001 0000 0000 0000", "0001 0000 0000 0001"]),
        (9999999999999998, 9999999999999999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
    ],
)
def test_card_number_generator(start: int, end: int, expected: list) -> None:
    a = card_number_generator(start, end)
    assert list(a) == expected


def test_card_number_generator_out_of_range() -> None:
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(9999999999999999, 10000000000000000))
    assert str(exc_info.value) == "Генерация невозможна"
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(-1, 1))
    assert str(exc_info.value) == "Генерация невозможна"

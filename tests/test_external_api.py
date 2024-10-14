from unittest.mock import patch

from src.external_api import convert_to_rub, get_transaction_amount


@patch("requests.get")
def test_convert_to_rub(mock_get) -> None:
    """Тест на конвертацию валюты."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 10},
        "info": {"timestamp": 1728766623, "rate": 95.676332},
        "date": "2024-10-12",
        "result": 956.76332,
    }
    assert convert_to_rub(currency_code="USD", amount=10) == 956.76


def test_get_rub_transaction_amount(rub_transaction_data: dict) -> None:
    assert get_transaction_amount(rub_transaction_data) == 31957.58


# def test_get_transaction_amount_empty():
#     assert get_transaction_amount({}) == []


# def test_get_transaction_amount_empty() -> None:
#     with pytest.raises(TypeError) as exc_info:
#         get_transaction_amount([])
#     assert str(exc_info.value) == "Сумма не найдена"


@patch("requests.get")
def test_get_usd_transaction_amount(mock_get, usd_transaction_data: dict) -> None:
    """Проверка вывода суммы в рублях по долларовой транзакции"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 10},
        "info": {"timestamp": 1728766623, "rate": 95.676332},
        "date": "2024-10-12",
        "result": 956.76332,
    }
    assert get_transaction_amount(usd_transaction_data) == 956.76


@patch("requests.get")
def test_get_eur_transaction_amount(mock_get, eur_transaction_data: dict) -> None:
    """Проверка вывода суммы в рублях по долларовой транзакции"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 10},
        "info": {"timestamp": 1728766623, "rate": 100.00},
        "date": "2024-10-12",
        "result": 1000.00,
    }
    assert get_transaction_amount(eur_transaction_data) == 1000.00

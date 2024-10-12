from unittest.mock import mock_open, patch

from src.utils import get_transactions_data


@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100, "currency": "USD"}]')
def test_valid_file(mock_file: str) -> None:
    """Тест на корректный файл."""
    transactions = get_transactions_data("../data/operations.json")
    assert transactions == [{"amount": 100, "currency": "USD"}]


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_empty_file(mock_file: str) -> None:
    """Тест на пустой файл."""
    transactions = get_transactions_data("../data/operations.json")
    assert transactions == []


@patch("builtins.open", new_callable=mock_open, read_data="123")
def test_incorrect_data(mock_file: str) -> None:
    """Тест на некорректные данные в файле."""
    transactions = get_transactions_data("../data/operations.json")
    assert transactions == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_file: str) -> None:
    """Тест на ошибку 'Файл не найден'."""
    transactions = get_transactions_data("../data/operations.json")
    assert transactions == []

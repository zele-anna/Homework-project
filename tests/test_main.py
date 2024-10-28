from unittest.mock import patch

from main import file_type_option, sort_by_date_option, state_option

transaction_list_sample = [
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
]


@patch("main.read_csv")
@patch("main.input")
def test_file_type_option(mocked_input, mock_read_csv) -> None:
    mocked_input.return_value = 2
    mock_read_csv.return_value = transaction_list_sample
    assert file_type_option() == transaction_list_sample


@patch("main.input")
def test_state_option(mock_input) -> None:
    mock_input.return_value = "EXECUTED"
    assert state_option(transaction_list_sample) == transaction_list_sample


@patch("main.input")
def test_sort_by_date_option(mock_input) -> None:
    mock_input.return_value = "да"
    assert sort_by_date_option(transaction_list_sample) == transaction_list_sample


@patch("main.input")
def test_filter_rub_option(mock_input) -> None:
    mock_input.return_value = "да"
    assert sort_by_date_option(transaction_list_sample) == transaction_list_sample


@patch("main.input")
def test_filter_by_word_option(mock_input) -> None:
    mock_input.return_value = "да"
    assert sort_by_date_option(transaction_list_sample) == transaction_list_sample

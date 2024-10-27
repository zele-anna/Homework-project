from unittest.mock import patch
from main import main

@patch('main.filter_by_word_option')
@patch('main.filter_rub_option')
@patch('main.sort_by_date_option')
@patch('main.state_option')
@patch('main.file_type_option')
# def test_main(mock_file_type_option, mock_state_option, mock_sort_by_date_option, mock_filter_rub_option, mock_filter_by_word_option):
#     mock_file_type_option.return_value = [
#         {
#             "id": 441945886,
#             "state": "CANCELED",
#             "date": "2019-10-26T10:50:58.294041",
#             "operationAmount": {"amount": 200.00, "currency": {"name": "EUR", "code": "EUR"}},
#             "description": "Перевод с карты на карту",
#             "from": "Maestro 1596837868705200",
#             "to": "Счет 64686473678894779200",
#         },
#     ]
#     mock_state_option.return_value = [
#         {
#             "id": 441945886,
#             "state": "CANCELED",
#             "date": "2019-10-26T10:50:58.294041",
#             "operationAmount": {"amount": 200.00, "currency": {"name": "EUR", "code": "EUR"}},
#             "description": "Перевод с карты на карту",
#             "from": "Maestro 1596837868705200",
#             "to": "Счет 64686473678894779200",
#         },
#     ]
#     mock_sort_by_date_option.return_value = [
#         {
#             "id": 441945886,
#             "state": "CANCELED",
#             "date": "2019-10-26T10:50:58.294041",
#             "operationAmount": {"amount": 200.00, "currency": {"name": "EUR", "code": "EUR"}},
#             "description": "Перевод с карты на карту",
#             "from": "Maestro 1596837868705200",
#             "to": "Счет 64686473678894779200",
#         },
#     ]
#     mock_filter_rub_option.return_value = [
#         {
#             "id": 441945886,
#             "state": "CANCELED",
#             "date": "2019-10-26T10:50:58.294041",
#             "operationAmount": {"amount": 200.00, "currency": {"name": "EUR", "code": "EUR"}},
#             "description": "Перевод с карты на карту",
#             "from": "Maestro 1596837868705200",
#             "to": "Счет 64686473678894779200",
#         },
#     ]
#     mock_filter_by_word_option.return_value = [
#         {
#             "id": 441945886,
#             "state": "CANCELED",
#             "date": "2019-10-26T10:50:58.294041",
#             "operationAmount": {"amount": 200.00, "currency": {"name": "EUR", "code": "EUR"}},
#             "description": "Перевод с карты на карту",
#             "from": "Maestro 1596837868705200",
#             "to": "Счет 64686473678894779200",
#         },
#     ]
#     assert main() == ""

@patch('main.file_type_option.data_type_chosen')
@patch('main.filter_rub_option')
@patch('main.sort_by_date_option')
@patch('main.state_option')
@patch("src.reader.pd.read_excel")
@patch('main.file_type_option')
def test_main(mock_data_type_chosen, mock_reader, mock_state_option, mock_sort_by_date_option, mock_filter_rub_option, mock_filter_by_word_option):
    mock_data_type_chosen.return_value = "2"
    mock_reader.return_value = [
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
    mock_state_option.return_value = "canceled"
    mock_sort_by_date_option.return_value = "нет"
    mock_filter_rub_option.return_value = "нет"
    mock_filter_by_word_option.return_value = "вклад"
    assert main() == ""

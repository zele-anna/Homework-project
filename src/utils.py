import json
from typing import Any


def get_transactions_data(path: str) -> Any:
    """Получает информацию о транзакциях из переданного в качестве переменной файла"""
    try:
        with open(path) as file:
            try:
                transactions_data = json.load(file)
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []
    return transactions_data

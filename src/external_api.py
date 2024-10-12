import os
from typing import Any, Union

import requests
from dotenv import load_dotenv


def get_transaction_amount(transaction: dict) -> Union[float, Any]:
    """Получает данные о транзакции и выводит сумму транзакции в рублях."""
    try:
        amount = transaction["operationAmount"]["amount"]
    except TypeError:
        return "Сумма не найдена"
    currency_code = transaction["operationAmount"]["currency"]["code"]
    if currency_code in ["USD", "EUR"]:
        amount = convert_to_rub(currency_code, amount)
    return amount


def convert_to_rub(currency_code: str, amount: float) -> Union[float, Any]:
    """Конвертация переданной суммы в переданной валюте в рубли."""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
    load_dotenv()
    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        rub_amount = round(response.json()["result"], 2)
        return rub_amount
    else:
        raise Exception(f"Код ошибки: {response.status_code}")


# print(convert_to_rub("USD", 10))

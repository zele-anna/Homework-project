from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_number: str) -> str:
    """Функция принимает тип и номер карты или счета и возвращает тип карты или счета и замаскированный номер"""
    result = ""
    if input_number.startswith("Счет"):
        result += "Счет " + get_mask_account(input_number)
    else:
        result += input_number[:-16] + get_mask_card_number(input_number[-16:])
    return result


def get_date(user_date: str) -> str:
    """Функция принимает дату в заданном формате и возвращает дату в формате ДД.ММ.ГГГГ."""
    date_format = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    # new_date = input_date[8:10] + "." + input_date[5:7] + "." + input_date[:4]
    return new_date

from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(input_number: str) -> str:
    """Функция принимает тип и номер карты или счета и возвращает тип карты или счета и замаскированный номер"""
    input_list = input_number.split(" ")

    if len(input_list) < 2:
        raise ValueError("Данные введены некорректно")

    type = ""
    number = ""
    for item in input_list:
        if item.isdigit():
            number += item
        else:
            type += item + " "
    result = ""
    if type.startswith("Счет"):
        result += type + get_mask_account(number)
    else:
        result += type + get_mask_card_number(number)
    return result


def get_date(user_date: str) -> str:
    """Функция принимает дату в заданном формате и возвращает дату в формате ДД.ММ.ГГГГ."""
    if user_date == "":
        raise ValueError("Дата не введена")

    date_format = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    # new_date = input_date[8:10] + "." + input_date[5:7] + "." + input_date[:4]
    return new_date

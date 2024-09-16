from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(input_number: str) -> str:
    if input_number.startswith("Счет"):
        result = "Счет " + get_mask_account(input_number)
    else:
        result = input_number[:-16] + get_mask_card_number(input_number[-16:])
    return result


def get_date(input_date: str) -> str:
    date = input_date[8:10] + "." + input_date[5:7] + "." + input_date[:4]
    return date

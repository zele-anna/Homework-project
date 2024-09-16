def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску,
    в которой скрыты символы с 7 по 12"""

    str_card_number = str(card_number)
    mask_card_number = str_card_number[:4] + " " + str_card_number[4:6] + "** **** " + str_card_number[-4:]
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску,
    в которой отображаются только последние 4 цифры номера счета"""

    return "**" + str(account_number)[-4:]

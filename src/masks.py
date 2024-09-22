def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску,
    в которой скрыты символы с 7 по 12"""

    if isinstance(card_number):
        card_number = str(card_number)

    if len(card_number) == 0:
        raise ValueError("Номер не введен")

    if len(card_number) != 16:
        raise ValueError("Введен некорректный номер")

    mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску,
    в которой отображаются только последние 4 цифры номера счета"""

    if isinstance(account_number):
        account_number = str(account_number)

    if len(account_number) != 20:
        raise ValueError("Введен некорректный номер счета")

    return "**" + account_number[-4:]

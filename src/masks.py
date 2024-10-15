import logging

logging.basicConfig(
    filename="logs/masks.log",
    filemode="w",
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    level=logging.DEBUG,
)

masks_logger = logging.getLogger("masks")


def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску,
    в которой скрыты символы с 7 по 12"""

    masks_logger.info("Маскировка номера карты...")

    if isinstance(card_number, int):
        masks_logger.debug("Преобразование числа в строку...")
        card_number = str(card_number)

    if len(card_number) == 0:
        masks_logger.error("Номер не введен")
        raise ValueError("Номер не введен")

    if len(card_number) != 16:
        masks_logger.error("Введен некорректный номер")
        raise ValueError("Введен некорректный номер")

    mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    masks_logger.info("Маскировка номера карты выполнена!")
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску,
    в которой отображаются только последние 4 цифры номера счета"""

    masks_logger.info("Маскировка номера счета...")
    if isinstance(account_number, int):
        masks_logger.debug("Преобразование числа в строку...")
        account_number = str(account_number)

    if len(account_number) != 20:
        masks_logger.error("Введен некорректный номер счета")
        raise ValueError("Введен некорректный номер счета")

    masks_logger.info("Маскировка номера счета выполнена!")
    return "**" + account_number[-4:]

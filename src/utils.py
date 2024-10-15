import json
import logging
from typing import Any

logging.basicConfig(
    filename="logs/utils.log",
    filemode="w",
    format="%(asctime)s %(filename)s %(levelname)s: %(message)s",
    level=logging.DEBUG,
)

utils_logger = logging.getLogger("utils")


def get_transactions_data(path: str) -> Any:
    """Получает информацию о транзакциях из переданного в качестве переменной файла"""
    utils_logger.info("Получение информации о транзакциях...")
    try:
        with open(path) as file:
            utils_logger.info("Успешное открытие файла.")
            try:
                transactions_data = json.load(file)
                if len(transactions_data) == 0:
                    utils_logger.warning("Получен пустой список!")
                    return []
            except json.JSONDecodeError:
                utils_logger.error("Ошибка декодирования!")
                return []
    except FileNotFoundError:
        utils_logger.error("Файл не найден!")
        return []
    utils_logger.info("Данные получены успешно!")
    return transactions_data

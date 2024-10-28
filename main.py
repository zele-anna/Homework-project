from charset_normalizer.md import is_accentuated

from src.generators import filter_by_currency
from src.processing import sort_by_date, filter_by_state
from src.reader import read_csv, read_excel
from src.search import search_via_description, category_counter
from src.utils import get_transactions_data
from src.widget import get_date, mask_account_card


def file_type_option() -> list:
    """Выбор типа входящих данных, получение данных из файла выбранного типа."""
    data_types = {1: "JSON", 2: "CSV", 3: "XLSX"}

    data_type_chosen = int(input(f"""Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из {data_types[1]}-файла
2. Получить информацию о транзакциях из {data_types[2]}-файла
3. Получить информацию о транзакциях из {data_types[3]}-файла\n"""))
    print(f"Для обработки выбран {data_types[data_type_chosen]}-файл.")

    transaction_list_raw = []
    if data_types[data_type_chosen] == "CSV":
        transaction_list_raw = read_csv("data/transactions.csv")
    elif data_types[data_type_chosen] == "XLSX":
        transaction_list_raw = read_excel("data/transactions_excel.xlsx")
    elif data_types[data_type_chosen] == "JSON":
        transaction_list_raw = get_transactions_data("data/operations.json")

    transaction_list = []
    for transaction in transaction_list_raw:
        if transaction:
            transaction_list.append(transaction)
    return transaction_list


def state_option(transaction_list: list) -> list:
    """Выбор статуса операций, фильтрация данных по выбранному статусу."""
    status_list = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status_to_filter = input(f"""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""").upper()
        if status_to_filter in status_list:
            transaction_list = filter_by_state(transaction_list, status_to_filter)
            print(f"Операции отфильтрованы по статусу {status_to_filter}")
            break
        else:
            print(f"Статус операции '{status_to_filter}' недоступен.")
    return transaction_list


def sort_by_date_option(transaction_list: list) -> list:
    """Выбор опции сортировки операций по дате, сортировка данных по выбранной опции."""
    sort_by_date_chosen = input("Отсортировать операции по дате? Да/Нет\n")
    if sort_by_date_chosen.lower() == "да":
        ascending_chosen = input("Отсортировать по возрастанию или по убыванию?\n")
        if ascending_chosen.lower() == "по возрастанию":
            is_reverse = False
        else:
            is_reverse = True
        transaction_list = sort_by_date(transaction_list, is_reverse)
    return transaction_list


def filter_rub_option(transaction_list: list) -> list:
    """Выбор опции фильтрации операций по валюте RUB, фильтрация данных по выбранному варианту."""
    rub_trans_chosen = input("Выводить только рублевые тразакции? Да/Нет\n")
    if rub_trans_chosen.lower() == "да":
        transaction_list = filter_by_currency(transaction_list, "RUB")
    return list(transaction_list)


def filter_by_word_option(transaction_list: list) -> list:
    """Выбор опции фильтрации операций по назначению платежа, фильтрация данных по переданной строке."""
    filter_by_word_chosen = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    if filter_by_word_chosen.lower() == "да":
        string_to_search = input("По какому слову отфильтровать список?\n")
        transaction_list = search_via_description(transaction_list, string_to_search)
    return transaction_list


def printing_results(transaction_list: list) -> list:
    """Вычисление и вывод результатов по полученному списку транзакций."""
    if len(transaction_list) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке: {len(transaction_list)}\n")

        for transaction in transaction_list:
            date = get_date(transaction.get("date"))
            # print(f"", end="")

            try:
                mask_from = mask_account_card(transaction["from"])
                print(f"{date} {transaction["description"]} {mask_from} -> ", end="")
            except KeyError:
                print(f"{date} {transaction["description"]} ", end="")
            except AttributeError:
                print(f"{date} {transaction["description"]} ", end="")

            mask_to = mask_account_card(transaction["to"])
            try:
                amount = transaction["amount"]
            except KeyError:
                amount = transaction["operationAmount"]["amount"]
            try:
                currency = transaction["currency_name"]
            except KeyError:
                currency = transaction["operationAmount"]["currency"]["name"]
            print(f"{mask_to} Сумма: {amount} {currency}")


def main():
    """Запуск программы"""

# Запрос параметров
    transaction_list = file_type_option()
    transaction_list = state_option(transaction_list)
    transaction_list = sort_by_date_option(transaction_list)
    transaction_list = filter_rub_option(transaction_list)
    transaction_list = filter_by_word_option(transaction_list)

# Вывод результата
    printing_results(transaction_list)

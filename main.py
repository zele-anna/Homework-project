from charset_normalizer.md import is_accentuated

from src.generators import filter_by_currency
from src.processing import sort_by_date, filter_by_state
from src.reader import read_csv, read_excel
from src.search import search_via_description, category_counter
from src.utils import get_transactions_data
from src.widget import get_date, mask_account_card


def main():
    """Запуск программы"""

    data_types = {1: "JSON", 2: "CSV", 3: "XLSX"}
    status_list = ["EXECUTED", "CANCELED", "PENDING"]

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

    while True:
        status_to_filter = input(f"""Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n""").upper()
        if status_to_filter in status_list:
            transaction_list = filter_by_state(transaction_list, status_to_filter)
            print(f"Операции отфильтрованы по статусу {status_to_filter}")
            break
        else:
            print(f"Статус операции '{status_to_filter}' недоступен.")

    sort_by_date_chosen = input("Отсортировать операции по дате? Да/Нет\n")
    if sort_by_date_chosen.lower() == "да":
        ascending_chosen = input("Отсортировать по возрастанию или по убыванию?\n")
        if ascending_chosen.lower() == "по возрастанию":
            is_reverse = False
        else:
            is_reverse = True
        transaction_list = sort_by_date(transaction_list, is_reverse)

    # try:
    #     print([x["currency_code"] for x in transaction_list])
    # except KeyError:
    #     print([x["operationAmount"]["currency"]["code"] for x in transaction_list])

    rub_trans_chosen = input("Выводить только рублевые тразакции? Да/Нет\n")
    if rub_trans_chosen.lower() == "да":
        transaction_list = filter_by_currency(transaction_list, "RUB")
    # try:
    #     print([x["currency_code"] for x in transaction_list])
    # except KeyError:
    #     print([x["operationAmount"]["currency"]["code"] for x in transaction_list])

    # print([x["description"] for x in transaction_list])

    filter_by_word_chosen = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    if filter_by_word_chosen.lower() == "да":
        string_to_search = input("По какому слову отфильтровать список?\n")
        transaction_list = search_via_description(transaction_list, string_to_search)

    # print([x["description"] for x in transaction_list])

    # categories_list = []
    # for trans in transaction_list:
    #     categories_set = set()
    #     categories_set.add(trans.get("description"))
    #     categories_list = list(categories_set)
    # category_count = category_counter(transaction_list, categories_list)

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


main()
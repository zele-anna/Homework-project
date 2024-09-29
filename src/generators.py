from turtledemo.penrose import start


def filter_by_currency(transaction_list, currency):
    return (x for x in transaction_list if x["operationAmount"]["currency"]["name"] == currency)


def transaction_descriptions(transaction_list):
    return (x["description"] for x in transaction_list)


def card_number_generator(start_num, stop_num):
    for number in range(start_num, stop_num+1):
        new_card_number = str(number)
        while len(new_card_number) < 16:
            new_card_number = "0" + new_card_number
        new_card_number = f"{new_card_number[0:4]} {new_card_number[4:8]} {new_card_number[8:12]} {new_card_number[12:16]}"
        yield new_card_number


# transactions = [
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {
#             "amount": "9824.07",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702"
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {
#             "amount": "79114.93",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188"
#     }
# ]

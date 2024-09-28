def filter_by_currency(transaction_dict, currency):
    return (x for x in transaction_dict if x["operationAmount"]["currency"]["name"] == currency)

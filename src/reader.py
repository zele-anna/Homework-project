import pandas as pd


def read_csv(path: str) -> list[dict]:
    """Чтение данных о транзакциях из файла формата csv."""
    df = pd.read_csv(path, delimiter=";")
    return df.to_dict(orient='records')


def read_excel(path: str) -> list[dict]:
    """Чтение данных о транзакциях из файла формата excel."""
    df = pd.read_excel(path)
    return df.to_dict(orient='records')

# if __name__ == "__main__":
#     result = read_excel("data/transactions_excel.xlsx")
#     print(result)
import pandas as pd


def read_csv(path: str) -> list[dict]:
    """Чтение данных о транзакциях из файла формата csv."""
    try:
        df = pd.read_csv(path, delimiter=";")
        return df.to_dict(orient="records")
    except FileNotFoundError:
        return []


def read_excel(path: str) -> list[dict]:
    """Чтение данных о транзакциях из файла формата excel."""
    try:
        df = pd.read_excel(path)
        return df.to_dict(orient="records")
    except FileNotFoundError:
        return []

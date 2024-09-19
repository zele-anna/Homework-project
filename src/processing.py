from typing import List


def filter_by_state(id_info: List[dict], state="EXECUTED") -> List[dict]:
    """Функция фильтрует информацию о id по ключу state (по умолчанию - EXECUTED)."""
    return [item for item in id_info if item["state"] == state]

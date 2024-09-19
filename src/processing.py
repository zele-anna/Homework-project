from typing import List


def filter_by_state(id_info: List[dict], state="EXECUTED") -> List[dict]:
    """Функция фильтрует информацию о id по ключу state (по умолчанию - EXECUTED)."""
    filtered_id = []
    for id in id_info:
        if id["state"] == state:
            filtered_id.append(id)
    return filtered_id

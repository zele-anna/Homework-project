from typing import List


def filter_by_state(id_info: List[dict], state: str = "EXECUTED") -> List[dict]:
    """Функция фильтрует информацию о id по ключу state (по умолчанию - EXECUTED)."""
    return [item for item in id_info if item["state"] == state]


def sort_by_date(id_info: List[dict], is_reverse: bool = True) -> List[dict]:
    """Функция сортирует информацию о id по дате (по умолчанию - по убыванию)."""
    return sorted(id_info, key=lambda x: x["date"], reverse=is_reverse)

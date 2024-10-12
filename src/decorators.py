from functools import wraps
from typing import Callable, Optional


def log(filename: Optional[str] = "no_file") -> Callable:
    """Декоратор, который проверяет работу функции и записывает лог с результатами в файл,
    имя которого опционально задается в параметрах декоратора, либо выводит лог в консоль,
    если наименование файла не задано."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
                if filename == "no_file":
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} ok\n")
            except Exception as er_info:
                if filename == "no_file":
                    print(f"{func.__name__} error: {er_info.__class__.__name__}. Inputs: {args}, {kwargs}")
                else:
                    with open(filename, "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} error: {er_info.__class__.__name__}. Inputs: {args}, {kwargs}\n")

        return wrapper

    return decorator

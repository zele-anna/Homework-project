from functools import wraps


def log(filename="no_file"):
    """Декоратор, который проверяет работу функции и записывает лог с результатами в файл,
    имя которого опционально задается в параметрах декоратора, либо выводит лог в консоль,
    если наименование файла не задано."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename == "no_file":
                    print(f"{func.__name__} ok")
                else:
                    with open(filename, "w", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} ok")
            except Exception as er_info:
                if filename == "no_file":
                    print(f"{func.__name__} error: {er_info.__class__.__name__}. Inputs: {args}, {kwargs}")
                else:
                    with open(filename, "w", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} error: {er_info.__class__.__name__}. Inputs: {args}, {kwargs}")
        return wrapper
    return decorator

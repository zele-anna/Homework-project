from typing import Any

from src.decorators import log


def test_log_console(capsys: Any) -> None:
    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(2, 3)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_console_division_error(capsys: Any) -> None:
    @log()
    def my_function(x: int, y: int) -> float:
        return x / y

    my_function(2, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: ZeroDivisionError. Inputs: (2, 0), {}\n"


def test_log_console_type_error_(capsys: Any) -> None:
    @log()
    def my_function(x: int, y: list) -> list:
        return [x for x in y]

    my_function(2, 5)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: TypeError. Inputs: (2, 5), {}\n"

from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("5500987611111234") == "5500 98** **** 1234"
    assert get_mask_card_number(5500987611111234) == "5500 98** **** 1234"


def test_get_mask_card_number_empty() -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
    assert str(exc_info.value) == "Номер не введен"


def test_get_mask_card_number_value_error() -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("123456781234567890")
    assert str(exc_info.value) == "Введен некорректный номер"


@pytest.mark.parametrize("account, expected", [("73654108430135874305", "**4305"), (73654108430135874305, "**4305")])
def test_get_mask_account(account: str, expected: str) -> None:
    assert get_mask_account(account) == expected


def test_get_mask_account_incorrect_number() -> Any:
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("")
        get_mask_account(0)
        get_mask_account(None)
        get_mask_account("123")
        get_mask_account("12345678")
        get_mask_account("1000200030004000123")
        get_mask_account("100020003000400012345")
    assert str(exc_info.value) == "Введен некорректный номер счета"

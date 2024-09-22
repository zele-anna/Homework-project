import pytest

from src.masks import get_mask_card_number
from src.masks import get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("5500987611111234") == "5500 98** **** 1234"
    assert get_mask_card_number(5500987611111234) == "5500 98** **** 1234"


def test_get_mask_card_number_empty():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
    assert str(exc_info.value) == "Номер не введен"


def test_get_mask_card_number_value_error():
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("123456781234567890")
    assert str(exc_info.value) == "Введен некорректный номер"


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("12345678") == "**5678"
    assert get_mask_account(12345678) == "**5678"

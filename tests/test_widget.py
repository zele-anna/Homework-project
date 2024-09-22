import pytest

from src.widget import mask_account_card
from src.widget import get_date

@pytest.mark.parametrize("input, expected",
                         [
                             ("Счет 12345678123456781234", "Счет **1234"),
                             ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
                             ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                             ("Visa Super Gold 7000792289606361", "Visa Super Gold 7000 79** **** 6361")])
def test_mask_account_card(input, expected):
    assert mask_account_card(input) == expected


def test_mask_account_card_incorrect_input():
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("")
        mask_account_card(0)
        mask_account_card("123")
        mask_account_card("Счет10002000300040005000")
    assert str(exc_info.value) == "Данные введены некорректно"


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_empty():
    with pytest.raises(ValueError) as exc_info:
        get_date("")
        get_date(0)
    assert str(exc_info.value) == "Дата не введена"

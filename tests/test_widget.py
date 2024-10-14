import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_num, expected",
    [
        ("Счет 12345678123456781234", "Счет **1234"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Super Gold 7000792289606361", "Visa Super Gold 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(input_num: str, expected: str) -> None:
    assert mask_account_card(input_num) == expected


def test_mask_account_card_incorrect_input() -> None:
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("")
        mask_account_card(0)
        mask_account_card("123")
        mask_account_card("Счет10002000300040005000")
    assert str(exc_info.value) == "Данные введены некорректно"


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_empty() -> None:
    with pytest.raises(ValueError) as exc_info:
        get_date("")
        get_date(0)
    assert str(exc_info.value) == "Дата не введена"

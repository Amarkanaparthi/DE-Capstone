from python_basics.utils import clean_name,parse_amount,summarize
import pytest

def test_clean_name_extra_spaces_and_case():
    assert clean_name("  aarav   SHARMA ") == "Aarav Sharma"

def test_clean_name_empty_string():
    assert clean_name("") == ""


def test_clean_name_single_word():
    assert clean_name("  priya ") == "Priya"



@pytest.mark.parametrize("text, expected", [
    ("1234.50", 1234.5),
    ("1,234.50", 1234.5),
    ("₹ 1,234.50", 1234.5),
    ("  99 ", 99.0),
])
def test_parse_amount_valid(text, expected):
    assert parse_amount(text) == expected


@pytest.mark.parametrize("bad", ["abc", "", "   ", "₹"])
def test_parse_amount_invalid(bad):
    with pytest.raises(ValueError):
        parse_amount(bad)

def test_parse_amount_negative():
    assert parse_amount("-1,200.00") == -1200.0

def test_summarize_normal():
    assert summarize([1.0, 2.0, 3.0]) == {"min": 1.0, "max": 3.0, "avg": 2.0}


def test_summarize_single_value():
    assert summarize([5.0]) == {"min": 5.0, "max": 5.0, "avg": 5.0}


def test_summarize_negative_values():
    assert summarize([-2.0, 4.0]) == {"min": -2.0, "max": 4.0, "avg": 1.0}


def test_summarize_empty_list():
    assert summarize([]) == {}

def test_summarize_zero_is_not_empty():
    assert summarize([0]) == {"min": 0, "max": 0, "avg": 0.0}

def test_summarize_decimals():
    assert summarize([0.1, 0.2, 0.3])["avg"] == pytest.approx(0.2)
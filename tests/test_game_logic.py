import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_get_range_for_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_get_range_for_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_get_range_for_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_get_range_for_unknown_defaults_normal():
    assert get_range_for_difficulty("Unknown") == (1, 100)


def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_guess_valid_float_truncates():
    ok, value, err = parse_guess("42.9")
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_guess_invalid():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


def test_parse_guess_empty():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_check_guess_win():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_check_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_check_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_check_guess_secret_as_string():
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"


def test_update_score_win_first_attempt():
    assert update_score(0, "Win", 1) == 90


def test_update_score_win_late_attempt_minimum():
    assert update_score(0, "Win", 20) == 10


def test_update_score_too_high_even():
    assert update_score(0, "Too High", 2) == 5


def test_update_score_too_high_odd():
    assert update_score(0, "Too High", 3) == -5


def test_update_score_too_low():
    assert update_score(10, "Too Low", 1) == 5


def test_edge_case_negative_guess():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5
    outcome, _ = check_guess(value, 50)
    assert outcome == "Too Low"


def test_edge_case_extremely_large_guess():
    ok, value, err = parse_guess("999999999999")
    assert ok is True
    assert value == 999999999999
    outcome, _ = check_guess(value, 50)
    assert outcome == "Too High"


def test_edge_case_decimal_small():
    ok, value, err = parse_guess("0.001")
    assert ok is True
    assert value == 0
    outcome, _ = check_guess(value, 1)
    assert outcome == "Too Low"


def test_edge_case_invalid_type_guess():
    outcome, message = check_guess("abc", 50)
    assert outcome == "Invalid"
    assert "invalid" in message.lower()

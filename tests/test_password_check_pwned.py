from powned.password import _check_pwned


def test_check_pwned_return_hits():
    suffix = "FE53E05116B108E1AF0F37D5EAC47CCB153"
    items = [f"{suffix}:2"]
    result = _check_pwned(suffix, items)
    assert result == 2


def test_check_pwned_return_zero():
    suffix = "YOUWONTFINDME"
    items = ["FE53E05116B108E1AF0F37D5EAC47CCB153:2"]
    result = _check_pwned(suffix, items)
    assert result == 0

import pytest

from powned.exceptions import InvalidPrefix
from powned.password import _get_pwned

from .mock_response import MockResponse


def mock_requests_get_with_results(*args, **kwargs):
    text = ("FE53E05116B108E1AF0F37D5EAC47CCB153:2\r\n"
            "FE672EE7C0EDF07657720BFA55067B6F42E:1\r\n"
            "FF79A7C061B33E14A16E54D63C36902EC77:4")
    return MockResponse(200, text)


def mock_requests_get_invalid_prefix(*args, **kwargs):
    return MockResponse(400, None)


def test_get_pwned_get_called(mocker):
    base_url = "https://api.pwnedpasswords.com/range/{}"
    mocked = mocker.patch("requests.get")
    _get_pwned("valid")
    mocked.assert_called_with(base_url.format("valid"))


def test_get_pwned_raises_invalid_prefix(mocker):
    """Tests invalid response raises InvalidPrefix exception."""
    mocker.patch("requests.get", new=mock_requests_get_invalid_prefix)
    with pytest.raises(InvalidPrefix):
        _get_pwned("invalid_prefix")


def test_get_pwned_returns_list_items(mocker):
    """Tests valid response returns list of items."""
    mocker.patch("requests.get", new=mock_requests_get_with_results)
    results = _get_pwned("valid")
    assert type(results) == list


def test_get_pwned_returns_valid_item(mocker):
    """Tests valid response returns valid first item."""
    mocker.patch("requests.get", new=mock_requests_get_with_results)
    results = _get_pwned("valid")
    suffix, hits = results[0].split(":")
    assert suffix == "FE53E05116B108E1AF0F37D5EAC47CCB153"
    assert hits == "2"

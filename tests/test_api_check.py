from powned.api import check
from .mock_response import MockResponse


def mock_requests_get(*args, **kwargs):
    text = "214943DAAD1D64C102FAEC29DE4AFE9DA3D:2413945"
    return MockResponse(200, text)


def test_check_returns_hits(mocker):
    mocker.patch("requests.get", new=mock_requests_get)
    hits = check("password1")
    assert hits == 2413945


def test_check_returns_none(mocker):
    mocker.patch("requests.get", new=mock_requests_get)
    hits = check("password2")
    assert hits == 0

from powned.password import _get_hexdigest


def test_get_sha1_calls_hexdigest(mocker):
    mocked = mocker.Mock()
    _get_hexdigest(mocked)
    mocked.hexdigest.assert_called_once()

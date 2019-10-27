from powned.password import _get_sha1


def test_get_sha1_calls_sha1(mocker):
    mocked_sha1 = mocker.patch("hashlib.sha1")
    _get_sha1("mystring")
    mocked_sha1.assert_called_once_with("mystring".encode())

import requests.exceptions


class MockResponse:
    def __init__(self, status, content):
        self._status_code = status
        self._content = content

    @property
    def status_code(self):
        return self._status_code

    @property
    def text(self):
        return str(self._content)

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.exceptions.HTTPError

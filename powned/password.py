import hashlib


def _get_sha1(str_input):
    encoded_input = str_input.encode()
    return hashlib.sha1(encoded_input)


def _get_hexdigest(hashed):
    return hashed.hexdigest()

import pytest

from src.base32768 import decode, encode


@pytest.mark.parametrize('s', [
    "",
    "ݡႢቤᖈ▟",
    "Ꞁ㙈ቡڀ㙈ƃ",
    "ڿ",
    "ဟ",
    "ꡟ",
    "ꡟꡟꡟ顐Ƈ",
    "ҠҠҠ㑏ʟ"
])
def test_decode_positive(s):
    assert encode(decode(s)) == s


@pytest.mark.parametrize('b', [
    b'',
    bytes([1, 2, 4, 8, 16, 32, 64, 128, 255]),
    bytes([255, 128, 64, 32, 16, 8, 4, 2, 1, 0]),
    (0).to_bytes(),
    (1).to_bytes(),
    (-1).to_bytes(signed=True),
    (2 ** 53 - 1).to_bytes(8, byteorder="little"),
    (-(2 ** 53)).to_bytes(8, signed=True, byteorder="little")
])
def test_encode_positive(b):
    assert decode(encode(b)) == b

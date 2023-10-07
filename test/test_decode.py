import pytest

from src.base32768 import decode


@pytest.mark.parametrize('expected, s', [
    (bytes([1, 2, 4, 8, 16, 32, 64, 128, 255]), "ݡႢቤᖈ▟"),
    (bytes([255, 128, 64, 32, 16, 8, 4, 2, 1, 0]), "Ꞁ㙈ቡڀ㙈ƃ"),
    ((0).to_bytes(), "ڿ"),
    ((1).to_bytes(), "ဟ"),
    ((-1).to_bytes(signed=True), "ꡟ"),
    ((2**53-1).to_bytes(8, byteorder="little"), "ꡟꡟꡟ顐Ƈ"),
    ((-(2**53)).to_bytes(8, signed=True, byteorder="little"), "ҠҠҠ㑏ʟ")
])
def test_decode_positive(expected, s):
    assert decode(s) == expected


def test_decode_empty():
    assert decode('') == b''


@pytest.mark.parametrize('t', [0, 1, 1.0, None, True, b''])
def test_decode_invalid_type(t):
    with pytest.raises(TypeError):
        decode(t)
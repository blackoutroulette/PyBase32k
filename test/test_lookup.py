from src.base32768 import _LOOKUP_ENC, _LOOKUP_DEC


def test_lookup_size():
    assert len(_LOOKUP_ENC) == 2
    assert len(_LOOKUP_ENC[7]) == 128
    assert len(_LOOKUP_ENC[15]) == 32768
    assert len(_LOOKUP_DEC) == 32896

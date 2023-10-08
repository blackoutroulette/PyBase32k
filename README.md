# PyBase32k
PyBase32k is a binary encoding optimised for UTF-16-encoded text.
It can be used to turn binary data into a string which can be safely copy and pasted. The bits to character ratio is 15:1.
For example encoding 2000 bits of data will result in a 134 character string. In comparison, base64, which has a 6:1 ratio, would result in a 334 character string.
This is a python3 port of https://github.com/qntm/base32768

# Install
```bash
git clone https://github.com/blackoutroulette/PyBase32k.git pybase32k
cd pybase32k
pip install .
```

# Usage
```python
import pybase32k

# Encode
encoded: str = pybase32k.encode(b'Hello World!')

# Decode
decoded: bytes = pybase32k.decode(encoded)
```

# License
MIT
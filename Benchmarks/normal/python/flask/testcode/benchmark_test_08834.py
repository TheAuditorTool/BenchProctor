# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import DES


def to_text(value):
    return str(value).strip()

def BenchmarkTest08834():
    raw_body = request.get_data(as_text=True)
    data = to_text(raw_body)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200

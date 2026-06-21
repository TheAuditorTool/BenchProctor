# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import DES


def BenchmarkTest38395():
    raw_body = request.get_data(as_text=True)
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(raw_body).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200

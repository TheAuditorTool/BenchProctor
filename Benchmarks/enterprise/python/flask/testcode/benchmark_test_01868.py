# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import DES


def BenchmarkTest01868():
    host_value = request.headers.get('Host', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    processed = data[:64]
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(processed).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200

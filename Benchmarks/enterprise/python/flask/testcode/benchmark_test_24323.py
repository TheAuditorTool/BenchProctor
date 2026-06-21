# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24323():
    referer_value = request.headers.get('Referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19970():
    header_value = request.headers.get('X-Custom-Header', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

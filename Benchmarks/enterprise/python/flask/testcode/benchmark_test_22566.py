# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest22566():
    header_value = request.headers.get('X-Custom-Header', '')
    data = normalise_input(header_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

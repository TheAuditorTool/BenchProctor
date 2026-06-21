# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81117():
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

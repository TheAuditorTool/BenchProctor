# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19321():
    cookie_value = request.cookies.get('session_token', '')
    ciphertext = bytes(b ^ 0x42 for b in str(cookie_value).encode())
    return jsonify({'length': len(ciphertext)}), 200

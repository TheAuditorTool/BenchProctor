# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22554():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

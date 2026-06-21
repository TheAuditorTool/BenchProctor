# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70915():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30490():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

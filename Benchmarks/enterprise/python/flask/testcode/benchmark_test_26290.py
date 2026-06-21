# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26290():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

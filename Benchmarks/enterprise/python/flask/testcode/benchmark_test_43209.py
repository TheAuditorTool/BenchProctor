# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43209():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38559():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

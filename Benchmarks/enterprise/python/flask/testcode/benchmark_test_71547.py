# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71547():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

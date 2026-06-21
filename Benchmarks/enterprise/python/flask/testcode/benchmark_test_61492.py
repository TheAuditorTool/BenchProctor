# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61492():
    auth_header = request.headers.get('Authorization', '')
    ciphertext = bytes(b ^ 0x42 for b in str(auth_header).encode())
    return jsonify({'length': len(ciphertext)}), 200

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10428():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

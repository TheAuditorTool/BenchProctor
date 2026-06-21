# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54562():
    origin_value = request.headers.get('Origin', '')
    ciphertext = bytes(b ^ 0x42 for b in str(origin_value).encode())
    return jsonify({'length': len(ciphertext)}), 200

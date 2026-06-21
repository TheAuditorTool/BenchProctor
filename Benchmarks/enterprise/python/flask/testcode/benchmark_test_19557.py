# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19557():
    origin_value = request.headers.get('Origin', '')
    data = str(origin_value).replace('\x00', '')
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

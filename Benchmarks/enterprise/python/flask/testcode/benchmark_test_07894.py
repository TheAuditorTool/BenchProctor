# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07894():
    origin_value = request.headers.get('Origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

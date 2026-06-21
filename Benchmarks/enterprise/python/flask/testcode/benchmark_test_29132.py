# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29132():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

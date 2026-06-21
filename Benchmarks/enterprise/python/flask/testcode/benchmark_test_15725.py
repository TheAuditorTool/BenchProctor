# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15725():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

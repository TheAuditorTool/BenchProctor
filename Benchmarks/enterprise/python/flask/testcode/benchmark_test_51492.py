# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51492():
    user_id = request.args.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12966():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

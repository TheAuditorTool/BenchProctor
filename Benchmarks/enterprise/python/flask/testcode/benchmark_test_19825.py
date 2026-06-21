# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19825():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

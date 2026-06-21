# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32426():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

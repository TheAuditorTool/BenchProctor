# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def BenchmarkTest02033():
    user_id = request.args.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    try:
        _bounded = int(data)
        if _bounded < 0 or _bounded > 10000:
            return jsonify({'error': 'out of range'}), 400
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    key = RSA.generate(512)
    ciphertext = PKCS1_OAEP.new(key).encrypt(str(data).encode()[:22])
    return jsonify({'length': len(ciphertext)}), 200

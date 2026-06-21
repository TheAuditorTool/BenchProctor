# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import AES


def BenchmarkTest34845():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(graphql_var).encode())
    return jsonify({'length': len(ciphertext)}), 200

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import AES


def BenchmarkTest33423():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data, _sep, _rest = str(json_value).partition('\x00')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

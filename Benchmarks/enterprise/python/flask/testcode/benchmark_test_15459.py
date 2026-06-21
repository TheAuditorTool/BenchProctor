# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from Crypto.Cipher import AES


def BenchmarkTest15459(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from Crypto.Cipher import AES


def BenchmarkTest22670(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return jsonify({'length': len(ciphertext)}), 200

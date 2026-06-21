# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from Crypto.Cipher import AES


def BenchmarkTest78033(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_GCM, nonce=b'000000000000')
    ciphertext = cipher.encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

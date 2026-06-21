# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from types import SimpleNamespace
from Crypto.Cipher import AES


def BenchmarkTest55629(path_param):
    path_value = path_param
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return jsonify({'length': len(ciphertext)}), 200

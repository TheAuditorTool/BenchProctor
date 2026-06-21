# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from Crypto.Cipher import AES


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest25570(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    key = b'0123456789abcdef'
    cipher = AES.new(key, AES.MODE_CBC, b'0000000000000000')
    ciphertext = cipher.encrypt(str(data).encode().ljust(16)[:16])
    return jsonify({'length': len(ciphertext)}), 200

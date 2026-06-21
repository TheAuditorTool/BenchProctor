# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from Crypto.Cipher import DES


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest01479(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200

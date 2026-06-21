# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from Crypto.Cipher import DES


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest25841():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200

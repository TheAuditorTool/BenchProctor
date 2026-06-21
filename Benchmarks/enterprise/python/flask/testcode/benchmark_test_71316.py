# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from Crypto.Cipher import DES


def BenchmarkTest71316(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    ciphertext = DES.new(b'8bytekey', DES.MODE_ECB).encrypt(str(data).encode().ljust(8)[:8])
    return jsonify({'length': len(ciphertext)}), 200

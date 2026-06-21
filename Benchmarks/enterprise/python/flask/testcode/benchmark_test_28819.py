# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest28819(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest80055(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

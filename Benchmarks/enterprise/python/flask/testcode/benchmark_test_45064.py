# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest45064(path_param):
    path_value = path_param
    data = relay_value(path_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

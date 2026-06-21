# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest43703(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

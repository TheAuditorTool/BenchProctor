# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79113():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

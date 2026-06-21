# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45402():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

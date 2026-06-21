# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13555():
    upload_name = request.files['upload'].filename
    ciphertext = bytes(b ^ 0x42 for b in str(upload_name).encode())
    return jsonify({'length': len(ciphertext)}), 200

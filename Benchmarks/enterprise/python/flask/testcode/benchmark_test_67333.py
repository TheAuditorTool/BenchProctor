# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67333():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

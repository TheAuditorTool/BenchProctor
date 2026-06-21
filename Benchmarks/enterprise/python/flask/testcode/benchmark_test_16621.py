# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16621():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

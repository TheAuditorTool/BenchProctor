# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58288():
    host_value = request.headers.get('Host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

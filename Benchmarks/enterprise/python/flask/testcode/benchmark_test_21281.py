# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21281():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

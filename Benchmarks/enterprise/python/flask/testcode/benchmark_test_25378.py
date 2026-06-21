# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25378():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

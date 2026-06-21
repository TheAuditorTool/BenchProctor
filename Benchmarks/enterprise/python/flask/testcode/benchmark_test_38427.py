# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38427():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json_value if json_value else 'default'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

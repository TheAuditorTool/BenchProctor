# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38016():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

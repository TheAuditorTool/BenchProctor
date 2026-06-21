# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53219():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

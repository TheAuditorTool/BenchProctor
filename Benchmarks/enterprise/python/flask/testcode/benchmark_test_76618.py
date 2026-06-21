# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76618():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

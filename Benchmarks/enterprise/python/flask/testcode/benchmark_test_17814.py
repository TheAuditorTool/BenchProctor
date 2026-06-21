# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17814():
    field_value = request.form.get('field', '')
    ciphertext = bytes(b ^ 0x42 for b in str(field_value).encode())
    return jsonify({'length': len(ciphertext)}), 200

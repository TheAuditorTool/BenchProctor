# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41716():
    multipart_value = request.form.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    ciphertext = bytes(b ^ 0x42 for b in str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200

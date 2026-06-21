# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32385():
    multipart_value = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    return jsonify({'error': 'An internal error occurred'}), 500

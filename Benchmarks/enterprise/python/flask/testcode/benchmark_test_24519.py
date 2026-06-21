# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24519():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    return jsonify({'error': 'An internal error occurred'}), 500

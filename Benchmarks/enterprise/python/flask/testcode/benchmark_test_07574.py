# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07574():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

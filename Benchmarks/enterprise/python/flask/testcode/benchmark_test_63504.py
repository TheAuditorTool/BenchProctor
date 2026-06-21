# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63504():
    field_value = request.form.get('field', '')
    parts = []
    for token in str(field_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

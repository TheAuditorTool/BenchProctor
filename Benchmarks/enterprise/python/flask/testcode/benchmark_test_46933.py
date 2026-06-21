# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46933():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30046():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500

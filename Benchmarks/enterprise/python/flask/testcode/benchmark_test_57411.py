# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57411():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    return jsonify({'error': 'An internal error occurred'}), 500

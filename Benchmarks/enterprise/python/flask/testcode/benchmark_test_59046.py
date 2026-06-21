# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59046():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    return jsonify({'error': 'An internal error occurred'}), 500

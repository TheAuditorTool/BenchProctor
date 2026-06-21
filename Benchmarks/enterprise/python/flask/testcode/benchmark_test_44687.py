# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest44687():
    field_value = request.form.get('field', '')
    data = default_blank(field_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

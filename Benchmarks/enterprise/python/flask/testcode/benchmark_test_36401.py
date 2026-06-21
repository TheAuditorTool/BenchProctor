# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest36401():
    multipart_value = request.form.get('multipart_field', '')
    data = default_blank(multipart_value)
    return jsonify({'error': 'An internal error occurred'}), 500

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43061():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    return jsonify({'error': 'An internal error occurred'}), 500

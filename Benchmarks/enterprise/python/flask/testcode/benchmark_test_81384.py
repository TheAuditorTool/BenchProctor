# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81384():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    return jsonify({'error': 'An internal error occurred'}), 500

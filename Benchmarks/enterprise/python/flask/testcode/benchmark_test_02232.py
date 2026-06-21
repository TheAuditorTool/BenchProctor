# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02232():
    field_value = request.form.get('field', '')
    data = f'{field_value}'
    return jsonify({'error': 'An internal error occurred'}), 500

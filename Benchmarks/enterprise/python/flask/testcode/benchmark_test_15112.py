# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15112():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    return jsonify({'error': 'An internal error occurred'}), 500

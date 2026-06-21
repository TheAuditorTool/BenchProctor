# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09386():
    field_value = request.form.get('field', '')
    return jsonify({'error': 'An internal error occurred'}), 500

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48492():
    field_value = request.form.get('field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    return jsonify({'error': 'An internal error occurred'}), 500

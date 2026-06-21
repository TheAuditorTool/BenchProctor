# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39678():
    field_value = request.form.get('field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

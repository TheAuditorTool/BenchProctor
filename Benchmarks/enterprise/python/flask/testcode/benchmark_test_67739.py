# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67739():
    multipart_value = request.form.get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    return jsonify({'error': 'An internal error occurred'}), 500

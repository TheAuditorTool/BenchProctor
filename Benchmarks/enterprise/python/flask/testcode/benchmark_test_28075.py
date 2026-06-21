# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28075():
    upload_name = request.files['upload'].filename
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    return jsonify({'error': 'An internal error occurred'}), 500

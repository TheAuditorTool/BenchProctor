# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08072():
    raw_body = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    return jsonify({'error': 'An internal error occurred'}), 500

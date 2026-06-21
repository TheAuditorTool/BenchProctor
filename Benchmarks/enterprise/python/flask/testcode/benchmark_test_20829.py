# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest20829():
    raw_body = request.get_data(as_text=True)
    data = ensure_str(raw_body)
    return jsonify({'error': 'An internal error occurred'}), 500

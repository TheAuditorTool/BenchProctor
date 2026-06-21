# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69477():
    raw_body = request.get_data(as_text=True)
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    return jsonify({'error': 'An internal error occurred'}), 500

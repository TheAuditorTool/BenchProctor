# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68019():
    raw_body = request.get_data(as_text=True)
    return jsonify({'error': 'An internal error occurred'}), 500

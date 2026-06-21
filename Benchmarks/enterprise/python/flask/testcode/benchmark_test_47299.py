# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47299():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72810():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    return jsonify({'error': 'An internal error occurred'}), 500

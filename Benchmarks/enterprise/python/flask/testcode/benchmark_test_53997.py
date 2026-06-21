# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53997():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    return jsonify({'error': 'An internal error occurred'}), 500

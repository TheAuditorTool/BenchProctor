# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40974():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500

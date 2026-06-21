# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30577():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    return jsonify({'error': 'An internal error occurred'}), 500

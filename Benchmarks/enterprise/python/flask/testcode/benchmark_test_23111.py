# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23111():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

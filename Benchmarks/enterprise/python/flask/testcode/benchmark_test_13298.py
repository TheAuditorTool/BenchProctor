# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13298():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

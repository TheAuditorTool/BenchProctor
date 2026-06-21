# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24683():
    ua_value = request.headers.get('User-Agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

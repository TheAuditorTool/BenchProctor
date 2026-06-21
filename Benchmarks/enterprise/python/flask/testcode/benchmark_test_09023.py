# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09023():
    ua_value = request.headers.get('User-Agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

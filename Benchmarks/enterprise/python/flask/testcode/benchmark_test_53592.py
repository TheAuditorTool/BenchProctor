# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53592():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

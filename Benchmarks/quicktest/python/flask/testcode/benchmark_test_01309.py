# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01309():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500

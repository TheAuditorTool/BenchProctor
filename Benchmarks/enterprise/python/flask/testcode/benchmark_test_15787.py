# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15787():
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    return jsonify({'error': 'An internal error occurred'}), 500

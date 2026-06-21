# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest48957():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    return jsonify({'error': 'An internal error occurred'}), 500

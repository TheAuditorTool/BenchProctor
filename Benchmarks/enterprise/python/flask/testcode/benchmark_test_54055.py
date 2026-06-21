# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54055():
    cookie_value = request.cookies.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    return jsonify({'error': 'An internal error occurred'}), 500

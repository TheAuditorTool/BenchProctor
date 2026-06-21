# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest17513():
    cookie_value = request.cookies.get('session_token', '')
    data = default_blank(cookie_value)
    return jsonify({'error': 'An internal error occurred'}), 500

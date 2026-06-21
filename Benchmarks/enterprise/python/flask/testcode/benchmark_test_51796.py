# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest51796():
    cookie_value = request.cookies.get('session_token', '')
    data = relay_value(cookie_value)
    return jsonify({'error': 'An internal error occurred'}), 500

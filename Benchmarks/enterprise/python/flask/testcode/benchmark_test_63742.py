# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63742():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    return jsonify({'error': 'An internal error occurred'}), 500

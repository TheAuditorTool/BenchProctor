# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46192():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    return jsonify({'error': 'An internal error occurred'}), 500

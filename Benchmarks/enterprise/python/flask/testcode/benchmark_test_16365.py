# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16365():
    cookie_value = request.cookies.get('session_token', '')
    return jsonify({'error': 'An internal error occurred'}), 500

# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest14363():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    return jsonify({'error': 'An internal error occurred'}), 500

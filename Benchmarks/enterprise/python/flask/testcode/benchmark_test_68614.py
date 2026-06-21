# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68614():
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    return jsonify({'error': 'An internal error occurred'}), 500

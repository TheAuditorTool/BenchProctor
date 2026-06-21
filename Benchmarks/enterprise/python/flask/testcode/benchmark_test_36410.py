# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36410():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    return jsonify({'error': 'An internal error occurred'}), 500

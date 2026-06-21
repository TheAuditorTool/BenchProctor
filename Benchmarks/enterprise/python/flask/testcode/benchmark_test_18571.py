# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18571():
    cookie_value = request.cookies.get('session_token', '')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(cookie_value)}

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest48027():
    cookie_value = request.cookies.get('session_token', '')
    data = ensure_str(cookie_value)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}

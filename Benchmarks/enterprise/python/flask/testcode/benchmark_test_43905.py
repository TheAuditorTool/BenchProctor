# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest43905():
    cookie_value = request.cookies.get('session_token', '')
    data = ensure_str(cookie_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

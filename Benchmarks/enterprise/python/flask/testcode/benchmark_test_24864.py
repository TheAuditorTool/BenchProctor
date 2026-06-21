# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest24864():
    cookie_value = request.cookies.get('session_token', '')
    data = normalise_input(cookie_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02880():
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

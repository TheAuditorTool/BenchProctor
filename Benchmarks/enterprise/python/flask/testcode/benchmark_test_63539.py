# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63539():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

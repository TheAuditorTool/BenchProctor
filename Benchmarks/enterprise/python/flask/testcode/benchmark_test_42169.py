# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42169():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

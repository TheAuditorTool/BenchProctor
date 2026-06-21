# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69506():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}

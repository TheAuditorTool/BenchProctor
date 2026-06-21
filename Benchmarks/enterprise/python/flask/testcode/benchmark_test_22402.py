# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22402():
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}

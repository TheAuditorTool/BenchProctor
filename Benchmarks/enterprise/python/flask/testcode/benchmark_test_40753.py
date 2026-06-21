# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40753():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}

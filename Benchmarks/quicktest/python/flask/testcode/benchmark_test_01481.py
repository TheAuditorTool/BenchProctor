# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01481():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}

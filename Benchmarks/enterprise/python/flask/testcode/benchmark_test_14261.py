# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14261():
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}

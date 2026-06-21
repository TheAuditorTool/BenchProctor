# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77790():
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}

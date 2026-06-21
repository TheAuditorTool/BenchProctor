# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27746():
    cookie_value = request.cookies.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}

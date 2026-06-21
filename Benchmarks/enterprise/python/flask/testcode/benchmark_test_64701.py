# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64701():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value}'
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}

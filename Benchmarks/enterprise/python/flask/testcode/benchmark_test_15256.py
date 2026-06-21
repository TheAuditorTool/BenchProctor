# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15256():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}

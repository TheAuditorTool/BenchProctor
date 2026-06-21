# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54162():
    cookie_value = request.cookies.get('session_token', '')
    if cookie_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = cookie_value
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}

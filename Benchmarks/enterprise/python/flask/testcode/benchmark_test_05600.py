# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05600():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})

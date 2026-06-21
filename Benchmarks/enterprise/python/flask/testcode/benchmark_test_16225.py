# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16225():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})

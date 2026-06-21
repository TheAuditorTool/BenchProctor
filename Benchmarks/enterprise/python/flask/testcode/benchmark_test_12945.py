# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12945():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})

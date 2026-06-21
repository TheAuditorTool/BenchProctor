# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49512():
    cookie_value = request.cookies.get('session_token', '')
    try:
        result = int(str(cookie_value))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})

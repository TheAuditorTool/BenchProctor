# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest74211():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})

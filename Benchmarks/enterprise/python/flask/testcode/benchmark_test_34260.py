# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34260():
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})

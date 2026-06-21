# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest78530():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})

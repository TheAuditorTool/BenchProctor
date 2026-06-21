# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30519():
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})

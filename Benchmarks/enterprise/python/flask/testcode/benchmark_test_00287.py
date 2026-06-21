# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00287():
    cookie_value = request.cookies.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})

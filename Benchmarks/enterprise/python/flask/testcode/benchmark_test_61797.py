# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61797():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})

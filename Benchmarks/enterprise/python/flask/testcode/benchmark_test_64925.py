# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64925():
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    int(str(data))
    return jsonify({"result": "success"})

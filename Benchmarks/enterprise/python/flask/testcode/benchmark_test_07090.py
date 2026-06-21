# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07090():
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})

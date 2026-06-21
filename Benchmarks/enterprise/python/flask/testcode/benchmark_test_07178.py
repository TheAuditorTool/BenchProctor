# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07178():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    eval(str(data))
    return jsonify({"result": "success"})

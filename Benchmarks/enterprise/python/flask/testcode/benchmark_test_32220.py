# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32220():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    eval(str(data))
    return jsonify({"result": "success"})

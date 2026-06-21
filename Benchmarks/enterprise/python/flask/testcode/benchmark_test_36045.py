# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36045():
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    eval(str(data))
    return jsonify({"result": "success"})
